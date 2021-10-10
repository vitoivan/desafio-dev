import './styles.css'
import { useUser } from '../../providers/user'
import { Redirect, Link } from 'react-router-dom'
import { useState, useEffect } from 'react';
import { useTransactions } from '../../providers/transactions';

const Header = () => {

    const { user, setUser } = useUser();
    const { setTransactions } = useTransactions();
    const [bar, setBar] = useState(false);
    
    useEffect(() => {
        
    }, [user])

    const handleClick = () => {
        setBar(!bar)
    }
    const logout = () => {
        setUser(undefined)
        setTransactions(undefined)
        localStorage.removeItem('@bycoders-desafio-dev')
    }

    const usr = localStorage.getItem('@bycoders-desafio-dev')
    if(usr && !user)
    {
        setUser(JSON.parse(usr))
    }
    if(!user?.profileObj){
        return <Redirect to='/login' />
    }

    return (
        <header className='header-container'>
            <h1>Olá, {user?.profileObj?.givenName}!</h1>
                <div className="header-menu-img">
                <div className="arrow"></div>
                <img src={user?.profileObj?.imageUrl} alt="profile" onClick={handleClick}/>
                <nav className={`menu${ bar ? " active" : "" }`}>
                    <ul>
                        <li><Link to='/'>Início</Link></li> 
                        <li><Link to='/registers' >Acessar registros</Link></li> 
                        <li onClick={logout}>Logout</li>
                    </ul>
                </nav>
            </div>
        </header>
    );
}

export default Header;