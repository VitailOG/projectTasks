import 'antd/dist/antd.css';
import './App.css';

import { Layout, Menu } from 'antd';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import Login from "./pages/auth/login";
import Home from "./pages/main/home";
import DetailProject from "./pages/main/detailProject";

const { Header, Content, Footer } = Layout;

function App() {
    return (
        <div className="App">
            <Layout className="layout" style={{ minHeight: "100vh" }}>
                <Header>
                    <div className="logo" />
                    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                        Задачі Проєків
                    </Menu>
                </Header>

                <Content style={{ padding: '0 50px' }}>
                    <div>
                        <Router>
                            <Switch>
                                <Route path="/login/" exact component={Login} />
                                <Route path="/home" exact component={Home} />
                                <Route path="/project/:id" exact component={DetailProject} />
                                <Redirect to='/login/' />
                            </Switch>
                        </Router>

                    </div>
                </Content>

                <Footer style={{ textAlign: 'center', background: '#c8c8c8' }}>
                    © 2021. Автор проєкта: Захарків Віталій vzaharkiv28@gmail.com
                </Footer>
            </Layout>
        </div>
    );
}

export default App;
