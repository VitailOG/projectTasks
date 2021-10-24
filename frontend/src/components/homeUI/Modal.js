import React, { useState } from 'react';
import { Modal, Input } from 'antd';

function ModalWindow(props) {

    return (
        <div>
            <Modal title={props.textTitle}
                visible={props.isModalVisible}
                onOk={props.handleOk}
                confirmLoading={props.isLoading}
                onCancel={props.handleCancel}
            >
                <Input placeholder="Назва проєкта"
                    value={props.newProject}
                    onChange={event => props.setNewProject(event.target.value)}
                />
            </Modal>
        </div>
    );
}

export default ModalWindow;