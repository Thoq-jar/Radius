import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from radius.html import Tags
from radius.base import Radius


def main():
    page = ""

    header = Tags.header(
        Tags.h1("Radius Demo App", tailwind="text-5xl text-center select-none cursor-default"),
        tailwind="flex flex-col justify-center items-center fixed top-0 w-full border-b border-neutral-600 p-10 backdrop-blur-md bg-black/20"
    )

    body = Tags.body(
        Tags.section(
            Tags.div(
                Tags.input(type="text", placeholder="Add new todo...", id="todo-input",
                          tailwind="p-2 rounded border border-neutral-600 bg-neutral-800 text-white w-64 mr-2") +
                Tags.button("Add", id="add-todo",
                           tailwind="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"),
                tailwind="flex justify-center mb-8 mt-4"
            ) +
            Tags.ul(id="todo-list", tailwind="space-y-2 w-96") +
            Tags.script("""
                document.addEventListener('DOMContentLoaded', () => {
                    const savedTodos = JSON.parse(localStorage.getItem('todos') || '[]');
                    savedTodos.forEach(todo => createTodoElement(todo.text, todo.checked));
                });

                document.getElementById('todo-input').addEventListener('keypress', (event) => {
                    if (event.key === 'Enter') addTodo();
                });

                document.getElementById('add-todo').addEventListener('click', addTodo);

                function saveTodos() {
                    const todos = Array.from(document.querySelectorAll('#todo-list li')).map(li => ({
                        text: li.querySelector('span').textContent,
                        checked: li.querySelector('input[type="checkbox"]').checked
                    }));
                    localStorage.setItem('todos', JSON.stringify(todos));
                }

                function createTodoElement(text, checked = false) {
                    const li = document.createElement('li');
                    li.className = 'flex justify-between items-center bg-neutral-800 p-3 rounded';
                    li.innerHTML = `
                        <div class="flex items-center">
                            <input type="checkbox"
                                   class="mr-3 h-5 w-5 rounded border-gray-300"
                                   ${checked ? 'checked' : ''}>
                            <span class="text-white ${checked ? 'line-through' : ''}">${text}</span>
                        </div>
                        <button class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600">
                            &times;
                        </button>
                    `;

                    li.querySelector('input[type="checkbox"]').addEventListener('change', function() {
                        this.nextElementSibling.classList.toggle('line-through');
                        saveTodos();
                    });

                    li.querySelector('button').addEventListener('click', function() {
                        this.parentElement.remove();
                        saveTodos();
                    });

                    document.getElementById('todo-list').appendChild(li);
                    return li;
                }

                function addTodo() {
                    const input = document.getElementById('todo-input');
                    if (input.value.trim()) {
                        createTodoElement(input.value);
                        saveTodos();
                        input.value = '';
                    }
                }
            """)
        ),
        tailwind="bg-black text-white flex flex-col max-w items-center justify-center mt-40"
    )

    footer = Tags.footer(
        Tags.p("© 2024 Radius Framework. All rights reserved.", tailwind="text-white"),
        tailwind="bg-black fixed bottom-0 w-full select-none text-center border-t border-neutral-600 p-2"
    )

    page = header + body + footer

    return page

if __name__ == "__main__":
    radius = Radius()

    # To make this accessable to your network (any computer connected to your wifi)
    # Set `expose=True` instead of False
    radius.serve(expose=False)
