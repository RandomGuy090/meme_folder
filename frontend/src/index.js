import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route} from "react-router-dom";
import React from 'react';
import { Provider } from 'react-redux'
import store from "./store/store.jsx"
import { createStore } from 'redux'
// import Header from './components/header.jsx'
import Mainpage from "./views/mainpage.jsx"
import "./style.css"



export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/*<Route path="/" element={<Layout />}>*/}
        <Route path="/" element={<Mainpage />} >
        

        </Route>
      </Routes>
    </BrowserRouter>
  );
}

const Store = createStore(store, [])
console.log(Store)

ReactDOM.render(
  
  <React.StrictMode>
    <Provider store={Store}> {/* HERE */}
      <App /> {/* Now, App is wrapped in Provider and hence can read from store */}
    </Provider>
  </React.StrictMode>
  , document.getElementById("root"));