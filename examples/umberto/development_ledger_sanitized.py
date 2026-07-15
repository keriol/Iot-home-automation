"""Public-safe example of a small SQLite development ledger.

This example demonstrates the structural ideas behind Umberto:

- tasks stored in SQLite
- deterministic status and priority ordering
- commit evidence linked to tasks
- no automatic Git operations
"""

from __future__ import annotations

import sqlite3
import tempfile
from dataclasses import dataclass
from pathlib import Path


STATUS_RANK = {
    "in_progress": 0,
    "review": 1,
    "ready": 2,
    "backlog": 3,
    "blocked": 4,
    "done": 5,
}

PRIORITY_RANK = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    priority TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS task_commits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id TEXT NOT NULL,
    commit_hash TEXT NOT NULL,
    note TEXT NOT NULL DEFAULT '',
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);
"""


@dataclass(frozen=True, slots=True)
class Task:
    id: str
    title: str
    status: str
    priority: str


class DevelopmentLedger:
    """Minimal deterministic task and evidence store."""

    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(SCHEMA)

    def add_task(
        self,
        task_id: str,
        title: str,
        *,
        status: str = "backlog",
        priority: str = "medium",
    ) -> None:
        if status not in STATUS_RANK:
            raise ValueError(f"Unsupported status: {status}")

        if priority not in PRIORITY_RANK:
            raise ValueError(f"Unsupported priority: {priority}")

        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO tasks (
                    id,
                    title,
                    status,
                    priority
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    task_id.strip().upper(),
                    title.strip(),
                    status,
                    priority,
                ),
            )

    def record_commit(
        self,
        task_id: str,
        commit_hash: str,
        note: str = "",
    ) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO task_commits (
                    task_id,
                    commit_hash,
                    note
                )
                VALUES (?, ?, ?)
                """,
                (
                    task_id.strip().upper(),
                    commit_hash.strip(),
                    note.strip(),
                ),
            )

    def list_open_tasks(self) -> list[Task]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT id, title, status, priority
                FROM tasks
                WHERE status NOT IN ('done', 'blocked')
                """
            ).fetchall()

        tasks = [
            Task(
                id=str(row["id"]),
                title=str(row["title"]),
                status=str(row["status"]),
                priority=str(row["priority"]),
            )
            for row in rows
        ]

        return sorted(
            tasks,
            key=lambda task: (
                STATUS_RANK[task.status],
                PRIORITY_RANK[task.priority],
                task.id,
            ),
        )

    def next_task(self) -> Task | None:
        tasks = self.list_open_tasks()
        return tasks[0] if tasks else None


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        database_path = Path(directory) / "ledger.sqlite"
        ledger = DevelopmentLedger(database_path)

        ledger.add_task(
            "DEMO-001",
            "Document the checkout workflow",
            status="ready",
            priority="high",
        )
        ledger.add_task(
            "DEMO-002",
            "Complete the current implementation",
            status="in_progress",
            priority="medium",
        )

        ledger.record_commit(
            "DEMO-002",
            "abc1234",
            "Implementation checkpoint",
        )

        selected = ledger.next_task()

        if selected is None:
            print("No actionable task.")
            return

        print(
            f"Selected: {selected.id} "
            f"[{selected.priority}] "
            f"{selected.status} - {selected.title}"
        )


if __name__ == "__main__":
    main()
