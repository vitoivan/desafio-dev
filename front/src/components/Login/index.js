import GoogleLogin from "react-google-login";
import './styles.css'
import { useUser } from '../../providers/user';
import Loading from '../Loading'

const Login = () => {

    const { setUser, loading, setLoading } = useUser();

    const responseGoogle = (resp) => {

        setUser(resp)
        setLoading(false)
    }

    const requested = () => {
        setLoading(true)
    }

    return (
        <div className="login-container">
            <h1>Bycoders Desafio-dev</h1>
            {
                loading === true ? (<Loading />):
                (<GoogleLogin
                    clientId="870034952037-38mq1nvbdbckdfe30d9keg5r7jtd945f.apps.googleusercontent.com"
                    buttonText="Continuar com o Google"
                    onSuccess={responseGoogle}
                    onFailure={responseGoogle}
                    onRequest={requested}
                />)
            }
            
        </div>
    );
}

export default Login;