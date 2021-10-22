import React, { useState, useEffect } from 'react';
import Column from "../../components/project/Column";
import AddButton from "../../components/homeUI/addButton";
import ModalWindow from '../../components/homeUI/Modal';
import axios from "axios";


function DetailProject({ match }) {

    const [isModalVisible, setIsModalVisible] = useState(false);
    const [columns, setColumns] = useState([])

    const [isLoading, setIsLoading] = useState(false);

    const [newProject, setNewProject] = useState('')

    const textButton = "Створити колонку";

    console.log(match.params.id)

    const showModal = () => {
        setIsModalVisible(true);
    };

    const handleOk = () => {
        setIsLoading(true)
        axios.post(`http://127.0.0.1:8000/task/${match.params.id}`, { title: newProject }).then(res => {
            if (res.data.Created) {
                let newColumns = { "id": res.data.id, "title": newProject, "project": match.params.id, "tasks": [] };
                setColumns([...columns, newColumns])
                setIsModalVisible(false)
                setNewProject('')
                setIsLoading(false)
            }
        })
    };

    const handleCancel = () => {
        setIsModalVisible(false);
    };


    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/task/test/${match.params.id}`).then(res => {
            setColumns(res.data)
        })
    }, [match.params.id])

    console.log(columns)

    return (
        <div className="App" style={{ display: 'flex', marginTop: '30px' }}>
            {columns.map(e => (
                <Column data={e}
                    setColumns={setColumns}
                    columns={columns}
                />
            ))}
            <ModalWindow isModalVisible={isModalVisible}
                handleOk={handleOk}
                handleCancel={handleCancel}
                setNewProject={setNewProject}
                newProject={newProject}
                isLoading={isLoading}
            />
            <AddButton text={textButton} showModal={showModal} />
        </div>
    );
}

export default DetailProject;
