import React, { Component } from 'react';
import {connect} from 'react-redux';
import { firebaseApp } from '../firebase';

class App extends Component {
    signOut() {
        firebaseApp.auth().signOut()
    }
    render() {
        return (
            <div>
                app
                <button
                className="btn btn-danger"
                
                onClick={this.signOut}
                >
                Sign Out
                </button>
            </div>
        )
    }
}

function mapStatetToProps(state){
    console.log('state', state);
    return {}
}

export default connect(mapStatetToProps, null)(App);