import { useContext, useState, createContext } from 'react'

const userCTX = createContext({})

export const UserProvider = ({children}) => {
    const [user, setUser] = useState(undefined);
    const [loading, setLoading] = useState(false);

    return (
        <userCTX.Provider value={{user, setUser, loading, setLoading}}>
            {children}
        </userCTX.Provider>
    );
}

export const useUser = () => useContext(userCTX)