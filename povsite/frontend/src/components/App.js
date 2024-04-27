import React, { Component, Fragment } from "react";

import "../styles/App.css";
import Header from "./Header"
import Main from "./Main";
import Footer from "./Footer";

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <Menu />
                <Block_1 />
                <Block_2 />
                <Block_3 />
                <Block_4 />
                <Block_5 />

                <Footer />
            </Fragment>
        );
    }
}

export default App;