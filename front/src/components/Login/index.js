import GoogleLogin from "react-google-login";
import './styles.css'
import { useUser } from '../../providers/user';
import Loading from '../Loading'
import { useHistory, Redirect } from "react-router";
import toast from "react-hot-toast";

const Login = () => {

    const { user, setUser, loading, setLoading } = useUser();
    const history = useHistory()
    const success = (resp) => {
        setUser(resp)
        setLoading(false)
        history.push('/')
    }
    const error = (resp) => {
        toast.error(resp.details)
        setLoading(false)
    }

    const requested = () => {
        setLoading(true)
    }

    const usr = localStorage.getItem('@bycoders-desafio-dev')
    if(usr && !user)
    {
        setUser(JSON.parse(usr))
    }
    if(user?.profileObj){
        return <Redirect to='/' />
    }
    
    return (
        <div className="login-container">
            <h1>Bycoders Desafio-dev</h1>
            {
                loading === true ? (<Loading />):
                (<GoogleLogin
                    clientId="520853830401-gp7q9qvs907hhv7n0r9tfrqgookf6oi3.apps.googleusercontent.com"
                    buttonText="Continuar com o Google"
                    onSuccess={success}
                    onFailure={error}
                    onRequest={requested}
                />)
            }
            
            
        </div>
    );
}

export default Login;