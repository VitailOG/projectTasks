import React, { useState, useEffect } from 'react';
import { Button, Affix } from 'antd';

function AddButton(props) {

    return (
        <Affix style={{ position: 'absolute', bottom: '85px', left: '45%' }}>
            <Button type="primary" onClick={props.showModal}>
                {props.text}
            </Button>
        </Affix>
    );
}

export default AddButton;
