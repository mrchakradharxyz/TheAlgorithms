"""
Python >= 3.10.0
"""
import linked_list, double_linked_list, stack_using_ll, circular_linked_list
import os, sys

sill = linked_list
dll = double_linked_list.DoublyLinkedList()
stll = stack_using_ll
cll = circular_linked_list


def cls():
    os.system("cls" if sys.platform == "win32" else "clear")


def _sill():
    try:
        data = input("Enter initial data: ")
        head = sill.Node(int(data))  # store numbers as int for consistency

        def options():
            print("\n=== Single Linked List Menu ===")
            print("1. Add at TOP")
            print("2. Add at END")
            print("3. Add at POS")
            print("4. Delete At TOP")
            print("5. Delete At END")
            print("6. Delete at POS")
            print("7. Display")
            print("8. Free all")
            print("9. Back to Main Menu")
            print("0. Exit")

        while True:
            cls()
            options()
            choice = input("Enter choice: ")

            try:
                match int(choice):
                    case 1:
                        data = int(input("Enter data: "))
                        head = sill.add_at_top(data, head)
                        print("Insert Done")

                    case 2:
                        data = int(input("Enter data: "))
                        head = sill.add_at_end(data, head)
                        print("Insert Done")

                    case 3:
                        data = int(input("Enter data: "))
                        pos = int(input("Enter position (0-based index): "))
                        head = sill.add_at_pos(data, pos, head)
                        print("Insert Done")

                    case 4:
                        head = sill.delete_at_top(head)
                        print("Deletion Done")

                    case 5:
                        head = sill.delete_at_end(head)
                        print("Deletion Done")

                    case 6:
                        pos = int(input("Enter position (0-based index): "))
                        head = sill.delete_at_pos(pos, head)
                        print("Deletion Done")

                    case 7:
                        if head:
                            sill.traverse(head)
                        else:
                            print("List is empty.")

                    case 8:
                        head = sill.free_all(head)
                        print("All nodes freed. List is now empty.")

                    case 9:
                        return  # go back to main menu

                    case 0:
                        sys.exit(0)

                    case _:
                        print("Invalid choice")

            except ValueError:
                print("Please enter a valid integer.")
            except Exception as e:
                print(f"Error: {e}")

            input("\nPress Enter to continue...")

    except KeyboardInterrupt:
        print("\nExiting..")
    except Exception as e:
        print(f"Error: {e}")
        main()

def _dll():
    try:

        # optional: ask initial data
        init = input("Enter initial data (or leave empty): ").strip()
        if init:
            dll.add_at_top(init)

        def options():
            print("\n=== Doubly Linked List Menu ===")
            print("1. Add at TOP")
            print("2. Add at END")
            print("3. Insert AFTER value")
            print("4. Delete At TOP")
            print("5. Delete At END")
            print("6. Delete by VALUE")
            print("7. Display FORWARD")
            print("8. Display REVERSE")
            print("9. Free all")
            print("10. Back to Main Menu")
            print("0. Exit")

        while True:
            cls()
            options()
            choice = input("Enter choice: ")

            try:
                match int(choice):
                    case 1:
                        data = input("Enter data: ")
                        dll.add_at_top(data)
                        print("Insert Done")

                    case 2:
                        data = input("Enter data: ")
                        dll.add_at_end(data)
                        print("Insert Done")

                    case 3:
                        after_value = input("Insert after value: ")
                        data = input("Enter data: ")
                        dll.insert_after(after_value, data)

                    case 4:
                        dll.delete_at_top()
                        print("Deletion Done")

                    case 5:
                        dll.delete_at_end()
                        print("Deletion Done")

                    case 6:
                        data = input("Enter value to delete: ")
                        dll.delete_by_value(data)
                        print("Deletion Done")

                    case 7:
                        dll.traverse()

                    case 8:
                        dll.traverse_reverse()

                    case 9:
                        dll.free_all()

                    case 10:
                        return  # back to main menu

                    case 0:
                        sys.exit(0)

                    case _:
                        print("Invalid choice")

            except ValueError:
                print("Please enter a valid integer.")
            except Exception as e:
                print(f"Error: {e}")

            input("\nPress Enter to continue...")

    except KeyboardInterrupt:
        print("\nExiting..")
    except Exception as e:
        print(f"Error: {e}")
        main()


# MATCH CASE 3
def _cll():
    try:
        data = input("Enter initial data: ")
        head = None if data.strip() == "" else cll.createNode(int(data))

        def options():
            print("\n=== Circular Singly Linked List Menu ===")
            print("1. Add at TOP")
            print("2. Add at END")
            print("3. Feature Incoming")
            print("4. Delete At TOP")
            print("5. Delete At END")
            print("6. Delete By Value")
            print("7. Display")
            print("8. Free all")
            print("9. Back to Main Menu")
            print("0. Exit")

        while True:
            cls()
            options()
            choice = input("Enter choice: ")

            try:
                match int(choice):
                    case 1:
                        data = int(input("Enter data: "))
                        head = cll.insertAtTop(data, head)
                        print("Insert Done")

                    case 2:
                        data = int(input("Enter data: "))
                        head = cll.insertAtEnd(data, head)
                        print("Insert Done")

                    case 3:
                        print("Feature Incoming")

                    case 4:
                        head = cll.deleteAtTop(head)
                        print("Deletion Done")

                    case 5:
                        head = cll.deleteAtEnd(head)
                        print("Deletion Done")

                    case 6:
                        val = int(input("Enter value to delete: "))
                        head = cll.deleteByValue(head, val)
                        print("Deletion Done")

                    case 7:
                        if head:
                            cll.display(head)
                        else:
                            print("List is empty.")

                    case 8:
                        head = cll.free_all(head)
                        print("All nodes freed. List is now empty.")

                    case 9:
                        return

                    case 0:
                        sys.exit(0)

                    case _:
                        print("Invalid choice")

            except ValueError:
                print("Please enter a valid integer.")
            except Exception as e:
                print(f"Error: {e}")

            input("\nPress Enter to continue...")

    except KeyboardInterrupt:
        print("\nExiting..")
    except Exception as e:
        print(f"Error: {e}")
        main()
def _stll():
    try:
        data = input("Enter initial data (leave blank for empty stack): ").strip()
        head = None if data == "" else stll.createNode(int(data))

        def options():
            print("\n=== Stack (Singly Linked List) Menu ===")
            print("1. PUSH")
            print("2. POP")
            print("3. PEEK")
            print("4. SIZE")
            print("5. DISPLAY")
            print("6. Back to Main Menu")
            print("0. Exit")

        while True:
            cls()
            options()
            choice = input("Enter choice: ")

            try:
                match int(choice):
                    case 1:
                        data = int(input("Enter data: "))
                        head = stll.push(data, head)
                        print("PUSH Done")

                    case 2:
                        head, popped = stll.pop(head)
                        if popped is not None:
                            print(f"POP Done. Removed: {popped}")

                    case 3:
                        top = stll.peek(head)
                        if top is not None:
                            print(f"Top element: {top}")

                    case 4:
                        print(f"Stack size: {stll.size(head)}")

                    case 5:
                        stll.display(head)

                    case 6:
                        return

                    case 0:
                        sys.exit(0)

                    case _:
                        print("Invalid choice")

            except ValueError:
                print("Please enter a valid integer.")
            except Exception as e:
                print(f"Error: {e}")

            input("\nPress Enter to continue...")

    except KeyboardInterrupt:
        print("\nExiting..")
    except Exception as e:
        print(f"Error: {e}")
        main()


def main():
    while True:
        cls()
        print("=== Data Structures CLI ===")
        print("1. Single Linked List")
        print("2. Double Linked List")
        print("3. Circular Linked List (coming soon)")
        print("4. Stack using Linked List")
        print("0. Exit")

        try:
            choice = int(input("Enter choice: "))
            match choice:
                case 1:
                    _sill()
                case 2:
                    _dll()
                case 3:
                    _cll()
                case 4:
                    _stll()
                case 0:
                    sys.exit(0)
                case _:
                    print("Invalid choice")
                    input("Press Enter...")
        except ValueError:
            print("Please enter a valid integer.")
            input("Press Enter...")


if __name__ == "__main__":
    main()
