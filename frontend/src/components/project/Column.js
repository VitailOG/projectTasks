import React, { useState, Fragment } from 'react';
import { Button, Card, Input } from "antd";
import Item from "./Item";
import axios from "axios";


function Column(props) {

    // check exist edit process
    const [isEdit, setIsEdit] = useState(false)
    const [idOfTheChangedTask, setIdOfTheChangedTask] = useState(0)

    // load buttun put
    const [isFetch, setIsFetch] = useState(false)

    // task and add input
    const [addTask, setAddTask] = useState(0)
    const [tasks, setTasks] = useState(props.data.tasks || [])

    // add new task input
    const [value, setValue] = useState('')

    // change title task
    const [newTask, setNewTask] = useState('')

    let createTask = (id) => {
        if (value.trim()) {
            setIsFetch(true)
            axios.post(`http://127.0.0.1:8000/task/create/${id}`, { "text": value }).then(res => {
                let newObj = { "id": res.data.id, "text": value }
                let newTaskList = [...tasks, newObj]
                setTasks(tasks => newTaskList)
                setAddTask(addTask => 0)
                setValue('')
                setIsFetch(false)
            })
        }
    }

    let deleteTask = (id) => {
        axios.delete(`http://127.0.0.1:8000/task/delete/${id}`).then(res => {
            if (res.data.Delete) {
                let t = tasks.find(t => t.id === id)
                setTasks(tasks.filter(e => e !== t))
            }
        })
    }

    let editTaskValue = (id) => {
        axios.patch(`http://127.0.0.1:8000/task/update/${id}`, { "text": newTask }).then(res => {
            if (res.data.Update) {
                let t = tasks.find(t => t.id === id)
                let index = tasks.indexOf(t);
                tasks[index]['text'] = newTask;
                setTasks(tasks);
                setIsEdit(false);
            }
        })
    }

    let deleteColumn = () => {
        axios.delete(`http://127.0.0.1:8000/task/${props.data.id}`).then(res => {
            if (res.data.Delete) {
                props.setColumns(props.columns.filter(e => e.id !== props.data.id))
            }
        })
    }

    let closeInput = () => {
        setAddTask(addTask => 0)
        setValue('')
    }

    return (
        <Card title={props.data.title}
            bordered={false}
            style={{ width: 250, marginLeft: "30px" }}>
            <div>{tasks && tasks.map((e, i) => (<
                Item text={e}
                i={i}

                deleteTask={deleteTask}

                isEdit={isEdit}
                setNewTask={setNewTask}
                newTask={newTask}
                setIsEdit={setIsEdit}
                setIdOfTheChangedTask={setIdOfTheChangedTask}
                idOfTheChangedTask={idOfTheChangedTask}
            />
            ))}
                {[...Array(addTask).keys()].map((e, i) => (
                    <p>
                        <Input placeholder="Добавити завдання"
                            onChange={event => setValue(event.target.value)}
                            value={value}
                        />
                    </p>
                ))}
            </div>
            <div style={{ borderTop: '1px solid grey', paddingTop: '10px' }}>
                {isEdit ?
                    <Fragment >
                        <Button
                            onClick={() => editTaskValue(idOfTheChangedTask)}
                            style={{ marginBottom: '5px' }}
                            loading={isFetch}
                        >Оновити
                        </Button>
                        <br />
                        <Button onClick={() => setIsEdit(false)}
                            type="primary"
                        >Відмінити
                        </Button>
                    </Fragment>
                    :
                    !addTask ?
                        <Fragment>
                            <Button onClick={() => setAddTask(addTask => 1)}
                                style={{ marginBottom: '5px' }}
                            >Додати
                            </Button>
                            <br />
                            <Button
                                type="primary"
                                onClick={() => deleteColumn()}
                                danger
                                ghost
                            >Видалити колонку
                            </Button>
                        </Fragment>
                        :
                        <Fragment>
                            <Button
                                onClick={() => createTask(props.data.id)}
                                type="warning"
                                style={{ marginBottom: '5px' }
                                }>Зберегти
                            </Button>
                            <br />
                            <Button
                                onClick={() => closeInput()}
                                type="primary"
                            >Відмінити
                            </Button>
                        </Fragment>
                }
            </div>
        </Card>
    );
}

export default Column;