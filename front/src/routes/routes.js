import { Switch, Route } from 'react-router-dom'
import Login from '../components/Login'
import Home from '../components/Home'

const Routes = () => {
    
    return (
        <Switch>
            <Route component={Login} path='/login'/>
            <Route component={Home} path='/'/>
        </Switch>
    );
}

export default Routes