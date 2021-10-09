import './css/app.css'
import Routes from './routes/routes'
import { Toaster } from 'react-hot-toast'

function App() {
  return (
    <div className="App">
      <Routes />
      <Toaster />
    </div>
  );
}

export default App;
