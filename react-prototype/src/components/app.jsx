import React, { Component } from 'react';
import {connect} from 'react-redux';
import { firebaseApp } from '../firebase';
import AddPatient from './AddPatient';
import PatientList from './PatientList'
import Table from 'react-bootstrap/Table';

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
                    <Table width = "600px">
                        <td width="200px"><strong>Patient ID</strong></td>
                        <td width="200px"><strong>Room Number</strong></td>
                        <td width="200px"><strong>Risk Level</strong></td>
                    </Table>
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