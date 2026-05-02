import sqlite3
from rich.console import Console
from rich.table import Table
from typing import List

# CLI uchun konsol
console = Console()

# SQLite bazasi uchun o'zaro bog'lanish
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Tabelarning tuzilishi
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL
    )
''')

# Tabelaning tuzilishi uchun o'zaro bog'lanishni qayta bajarish
conn.commit()

# Funktsiya vazifalarni ro'yxatga qo'shish uchun
def add_task(title: str, description: str) -> None:
    cursor.execute('INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)', (title, description, 'not started'))
    conn.commit()

# Funktsiya vazifalarni ro'yxatdan olib tashlash uchun
def delete_task(id: int) -> None:
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()

# Funktsiya vazifalarni ro'yxatdan olib tashlash uchun
def update_task(id: int, title: str, description: str) -> None:
    cursor.execute('UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?', (title, description, 'in progress', id))
    conn.commit()

# Funktsiya vazifalarni ro'yxatga qo'shish uchun
def get_tasks() -> List[dict]:
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return [{'id': task[0], 'title': task[1], 'description': task[2], 'status': task[3]} for task in tasks]

# CLI uchun funksiyalar
def main():
    while True:
        console.print('[bold magenta]Vazifalar menejeri[/bold magenta]')
        console.print('[bold]1[/bold]. Vazifalarni ro'yxatga qo'shish')
        console.print('[bold]2[/bold]. Vazifalarni ro'yxatdan olib tashlash')
        console.print('[bold]3[/bold]. Vazifalarni ro'yxatdan olib tashlash')
        console.print('[bold]4[/bold]. Vazifalarni ro'yxatga qo'shish')
        console.print('[bold]5[/bold]. Chiqish')
        choice = console.input('[bold]Izoh: [/bold]')
        
        if choice == '1':
            title = console.input('[bold]Vazifa nomi: [/bold]')
            description = console.input('[bold]Vazifa tavsifi: [/bold]')
            add_task(title, description)
        elif choice == '2':
            id = int(console.input('[bold]Vazifa ID: [/bold]'))
            delete_task(id)
        elif choice == '3':
            id = int(console.input('[bold]Vazifa ID: [/bold]'))
            title = console.input('[bold]Vazifa nomi: [/bold]')
            description = console.input('[bold]Vazifa tavsifi: [/bold]')
            update_task(id, title, description)
        elif choice == '4':
            tasks = get_tasks()
            table = Table(title="Vazifalar")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Nom", style="magenta")
            table.add_column("Tavsif", style="green")
            table.add_column("Holat", style="red")
            for task in tasks:
                table.add_row(str(task['id']), task['title'], task['description'], task['status'])
            console.print(table)
        elif choice == '5':
            break
        else:
            console.print('[bold red]Xato![/bold red]')

if __name__ == '__main__':
    main()
```

Bu kodda, vazifalarni ro'yxatga qo'shish, ro'yxatdan olib tashlash, ro'yxatdan olib tashlash va vazifalarni ro'yxatga qo'shish uchun funksiyalar mavjud. CLI uchun funksiyalar ham mavjud. Vazifalarni ro'yxatga qo'shish uchun, vazifa nomi va tavsifi kiritiladi. Vazifalarni ro'yxatdan olib tashlash uchun, vazifa ID kiritiladi. Vazifalarni ro'yxatdan olib tashlash uchun, vazifa ID, nomi va tavsifi kiritiladi. Vazifalarni ro'yxatga qo'shish uchun, vazifa ID, nomi va tavsifi kiritiladi.
