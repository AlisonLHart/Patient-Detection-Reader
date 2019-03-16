import React, { Component } from 'react';
import {connect} from 'react-redux';
import { firebaseApp } from '../firebase';
import AddPatient from './AddPatient';

class App extends Component {
    signOut() {
        firebaseApp.auth().signOut()
    }
    render() {
        return (
            <div>
                <div>
                    <h3>Patients</h3>
                    <AddPatient />
                    <div>Patient list</div>
                </div>
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