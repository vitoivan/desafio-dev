import { UserProvider } from "./user";
import { TransactionsProvider } from "./transactions";

const Providers = ({ children }) => {
    return (
        <UserProvider>
            <TransactionsProvider>
                {children}
            </TransactionsProvider>
        </UserProvider>
    );
}

export default Providers