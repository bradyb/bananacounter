import banana from './banana_generated.jpg';
import './App.css';

function App() {
  return (
    <div className="app">
      <div className="header">keep your eyes peeled</div>
      <img src={banana} className="banana" />
    </div>
  );
}

export default App;
