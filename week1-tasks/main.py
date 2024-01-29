import json
from rich.console import Console
from rich.table import Table

CONTACT_FILE = "contacts.json"

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=2)

def load_contacts():
    try:
        with open(CONTACT_FILE, 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    return contacts

def display_contacts(contacts):
    if not contacts:
        console.print("\n[yellow]No contacts found.[/yellow]\n")
        return

    table = Table(title="\n[cyan]Contacts[/cyan]")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Phone", style="green")
    table.add_column("Email", style="blue")

    for contact in contacts:
        table.add_row(
            str(contact["id"]),
            contact["name"],
            contact["phone"],
            contact["email"]
        )

    console.print(table)
    print()

def add_contact(contacts, name, phone, email):
    contact_id = len(contacts) + 1
    new_contact = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    console.print(f"\n[green]Contact added successfully. ID: {contact_id}[/green]\n")

def search_contact(contacts, search_term):
    results = [contact for contact in contacts if search_term.lower() in contact["name"].lower()]
    return results

def update_contact(contacts, contact_id, new_name, new_phone, new_email):
    for contact in contacts:
        if contact["id"] == contact_id:
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            save_contacts(contacts)
            console.print(f"\n[green]Contact with ID {contact_id} updated successfully.[/green]\n")
            return
    console.print(f"\n[yellow]Contact with ID {contact_id} not found.[/yellow]\n")

def delete_contact(contacts, contact_id):
    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)
            save_contacts(contacts)
            console.print(f"\n[green]Contact with ID {contact_id} deleted successfully.[/green]\n")
            return
    console.print(f"\n[yellow]Contact with ID {contact_id} not found.[/yellow]\n")

def main():
    contacts = load_contacts()

    while True:
        console.print("[cyan]1.[/cyan] Display Contacts")
        console.print("[cyan]2.[/cyan] Add Contact")
        console.print("[cyan]3.[/cyan] Search Contact")
        console.print("[cyan]4.[/cyan] Update Contact")
        console.print("[cyan]5.[/cyan] Delete Contact")
        console.print("[cyan]6.[/cyan] Exit")

        choice = console.input("[bold magenta]Enter your choice (1-5): [/bold magenta]")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            name = console.input("\n[bold]Enter name:[/bold] ")
            phone = console.input("[bold]Enter phone number:[/bold] ")
            email = console.input("[bold]Enter email address:[/bold] ")
            add_contact(contacts, name, phone, email)
        elif choice == '3':
            search_term = console.input("\n[bold]Enter name to search:[/bold] ")
            search_results = search_contact(contacts, search_term)
            display_contacts(search_results)
        elif choice == '4':
            contact_id = int(console.input("\n[bold]Enter contact ID to update:[/bold] "))
            new_name = console.input("[bold]Enter new name:[/bold] ")
            new_phone = console.input("[bold]Enter new phone number:[/bold] ")
            new_email = console.input("[bold]Enter new email address:[/bold] ")
            update_contact(contacts, contact_id, new_name, new_phone, new_email)
        elif choice == '5':
            contact_id = int(console.input("\n[bold]Enter contact ID to delete:[/bold] "))
            delete_contact(contacts, contact_id)
        elif choice == '6':
            console.print("\n[bold green]Exiting Contact Management System. Goodbye![/bold green]")
            break
        else:
            console.print("\n[bold red]Invalid choice. Please enter a number between 1 and 5.[/bold red]\n")


if __name__ == "__main__":
    console = Console()
    console.rule("[bold cyan]Contact Management System[/bold cyan]")
    main()
