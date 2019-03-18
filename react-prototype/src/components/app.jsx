import React, { Component } from 'react';
import {connect} from 'react-redux';
import { firebaseApp } from '../firebase';
import AddPatient from './AddPatient';
import PatientList from './PatientList'

class App extends Component {
    signOut() {
        firebaseApp.auth().signOut()
    }
    render() {
        return (
            <div style={{margin: '50px'}}>
                <div >
                    <h3>Patients</h3>
                    <AddPatient />
                    <PatientList/>
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
    //console.log('state', state);
    return {}
}

export default connect(mapStatetToProps, null)(App);