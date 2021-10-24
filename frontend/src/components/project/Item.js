import React, { useState, Fragment } from 'react';
import { EditOutlined, DeleteOutlined } from '@ant-design/icons';
import { Input } from "antd";

function Item(props) {
    const [isHover, setIsHover] = useState(false)
    const [edit, setEdit] = useState(false)

    let onMouse = () => {
        setIsHover(true)
    }

    let leaveMouse = () => {
        setIsHover(false)
    }

    let editTask = (task) => {
        props.setIsEdit(true)
        setEdit(true)
        props.setIdOfTheChangedTask(props.text.id)
        props.setNewTask(task)
    }

    return (
        <div onMouseEnter={onMouse}
            onMouseLeave={leaveMouse}
            style={{ background: '#ececec', padding: '5px 0px 0.5px 0px', margin: '10px 0px' }}>
            {
                edit && props.isEdit && props.idOfTheChangedTask === props.text.id
                    ?
                    <Input
                        placeholder="Добавити завдання"
                        onChange={event => props.setNewTask(event.target.value)}
                        value={props.newTask}
                    />
                    :
                    <p>{props.text.text}</p>
            }
            {
                isHover
                    ?
                    <Fragment>
                        <EditOutlined onClick={() => editTask(props.text.text)} />
                        <DeleteOutlined onClick={() => props.deleteTask(props.text.id)} />
                    </Fragment>
                    :
                    ""
            }
        </div>
    );
}

export default Item;