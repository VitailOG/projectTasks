import React from 'react';
import {Row, Col} from 'antd';
import CardProject from "./CardProject";

function Projects(props) {

    return (
        <div style={{ marginTop: '50px', marginLeft: '120px' }}>
            <Row gutter={[16, 24]}>
                {props.data.map(e =>(
                   <Col span={5} key={e.id}>
                        <CardProject e={e} deleteProject={props.deleteProject}/>
                   </Col>
                ))}
            </Row>
        </div>
    );
}

export default Projects;
