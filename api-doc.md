# API Documentation

> ℹ️ `relates_to` filed can be blank

## Endpoints:

### `GET /api/tasks`

Returns a list of tasks.

```
> GET /api/tasks

< 200 OK
{
  tasks: Task[] = [
    { id: number, label: string, completed: boolean, relates_to: obj }
  ]
}
```

### `POST /api/tasks`

Creates a new task.

```
> POST /api/tasks
{ label: string }

< 201 Created
{
  task: { id: number, label: string, completed: boolean, relates_to: obj }
}
```

### `POST /api/tasks/:id`

Updates the task of the given ID.

```
> POST /api/tasks/:id
{ label: string } |
{ completed: boolean } |
{ label: string, completed: boolean }

< 200 OK
{
  task: Task = { id: number, label: string, completed: boolean, relates_to: obj }
}

< 404 Not Found
{ error: string }
```

### `DELETE /api/tasks/:id`

Deletes the task of the given ID.

```
> DELETE /api/tasks/:id

< 204 No Content

< 404 Not Found
{ error: string }
```
