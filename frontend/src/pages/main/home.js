import React, { useState, useEffect } from 'react';
import ModalWindow from "../../components/homeUI/Modal";
import Projects from "../../components/homeUI/Projects";
import AddButton from '../../components/homeUI/addButton';
import axios from "axios";

function Home() {
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [data, setData] = useState([]);
    const [newProject, setNewProject] = useState('')

    const [isLoading, setIsLoading] = useState(false);

    const textButton = "Створити проєкт";


    {/*modal hook */ }
    const showModal = () => {
        setIsModalVisible(true);
    };

    const handleOk = () => {
        setIsLoading(true)
        axios.post('http://127.0.0.1:8000/project/', { title: newProject }).then(res => {
            if (res.data.success) {
                setData([...data, { "title": newProject, "id": res.data.id }])
                setIsModalVisible(false);
                setNewProject('');
                setIsLoading(false)
            }
        })
    };

    const handleCancel = () => {
        setIsModalVisible(false);
    };

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/project/').then(res => setData(res.data))
    }, [])


    let deleteProject = (id) => {
        axios.delete(`http://127.0.0.1:8000/project/${id}`)
            .then(res => {
                if (res.data.delete) {
                    setData(data.filter(e => e.id !== id))
                }
            })
    }

    return (
        <div>
            <Projects data={data} deleteProject={deleteProject} />
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

export default Home;