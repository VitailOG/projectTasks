import { Form, Input, Button, Col } from 'antd';
import React from 'react';
import { useHistory } from "react-router-dom";
import $axios from "../../http/index"

function Login() {
    const history = useHistory();

    const onFinish = (values) => {
        $axios.post('http://127.0.0.1:8000/auth/',
            { username: values.username, password: values.password }).then(res => {
                localStorage.setItem("token", res.data.token)
                history.push('/home/')
            }).catch(e => console.log(e))
    };

    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };

    return (
        <div>
            <Col span={12} offset={4} style={{ 'marginTop': '160px' }}>
                <Form
                    name="basic"
                    labelCol={{ span: 8 }}
                    wrapperCol={{ span: 16 }}
                    initialValues={{ remember: true }}
                    onFinish={onFinish}
                    onFinishFailed={onFinishFailed}
                    autoComplete="off"
                >
                    <Form.Item
                        label="Username"
                        name="username"
                        rules={[{ required: true, message: 'Please input your username!' }]}
                    >
                        <Input />
                    </Form.Item>

                    <Form.Item
                        label="Password"
                        name="password"
                        rules={[{ required: true, message: 'Please input your password!' }]}
                    >
                        <Input.Password />
                    </Form.Item>

                    <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                        <Button type="primary" htmlType="submit">
                            Submit
                        </Button>
                    </Form.Item>
                </Form>
            </Col>
        </div>
    );
}

export default Login;