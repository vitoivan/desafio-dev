import { useContext, useState, createContext, useEffect } from 'react'

const userCTX = createContext({})

export const UserProvider = ({children}) => {
    const [user, setUser] = useState(undefined);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const usr = localStorage.getItem('@bycoders-desafio-dev')
        if (!usr && user)
        {
            localStorage.setItem('@bycoders-desafio-dev', JSON.stringify(user))
        }
    }, [user])
    return (
        <userCTX.Provider value={{user, setUser, loading, setLoading}}>
            {children}
        </userCTX.Provider>
    );
}

export const useUser = () => useContext(userCTX)