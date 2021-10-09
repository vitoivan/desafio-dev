import { Switch, Route } from 'react-router-dom'
import Login from '../components/Login'
import Home from '../components/Home'
import Registers from '../components/Registers'

const Routes = () => {
    
    return (
        <Switch>
            <Route component={Login} path='/login'/>
            <Route component={Home} exact path='/'/>
            <Route component={Registers} path='/registers'/>
        </Switch>
    );
}

export default Routes