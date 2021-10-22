import React from 'react';
import {Card, Button} from 'antd';
import {CloseOutlined} from '@ant-design/icons';
import {Link} from "react-router-dom";

function CardProject(props) {

    return (
        <div className="site-card-wrapper">
           <Card title={props.e.title} bordered={false}>
               <CloseOutlined style={{ position: 'relative', left: '160px', top: '-67px', cursor: 'pointer'}}
                              onClick={() => props.deleteProject(props.e.id)}
               />
               <Button type="primary" style={{ position: 'relative', left: '60px', bottom: '-10px'}}>
                   <Link to={{ pathname:`/project/${props.e.id}`, fromDashboard: false }}>Детальніше</Link>
               </Button>
           </Card>
        </div>
    );
}

export default CardProject;
