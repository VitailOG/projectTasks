import axios from 'axios';

const $axios = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    withCredentials: true
});

$axios.interceptors.request.use((config) => {
    if (localStorage.getItem('token')) {
        config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
    }

    return config;
})

export default $axios;