import './styles.css'
import { useUser } from '../../providers/user'
import { Redirect } from 'react-router-dom'
import { useState } from 'react';
import { useTransactions } from '../../providers/transactions';

const Header = () => {

    const { user, setUser } = useUser();
    const { setTransactions } = useTransactions();
    const [bar, setBar] = useState(false);
    
    const handleClick = () => {
        setBar(!bar)
    }
    const logout = () => {
        setUser(undefined)
        setTransactions(undefined)
    }

    if(!user.profileObj){
        return <Redirect to='/login' />
    }

    return (
        <header className='header-container'>
            <h1>Olá, {user?.profileObj?.givenName}!</h1>
            <div className="header-menu-img">
                <img src={user?.profileObj?.imageUrl} alt="profile picture" onClick={handleClick}/>
                <nav className={`menu${ bar ? " active" : "" }`}>
                    <ul>
                        <li onClick={logout}>Logout</li>
                    </ul>
                </nav>
            </div>
        </header>
    );
}

export default Header;