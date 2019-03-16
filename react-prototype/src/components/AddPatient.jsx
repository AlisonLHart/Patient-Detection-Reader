import  React, { Component} from 'react';
import {patientRef} from '../firebase';

class AddPatient extends Component{
    constructor(props){
        super(props);
        this.state = {
            pid: '',
            rfid: ''
        }
    }

    addPatient(){
        console.log('this.state', this.state)
        patientRef.push({PID: 'test23', RFID: 'test12'})
    }
    render () {
        return (
            <div className="form-inline">
            <div className="form-group">
            <input 
                type="text"
                placeholder="patient ID"
                className="form-control"
                style={{marginRight: '5px'}}
                onChange={event => this.setState({pid: event.target.value})}
                />
                <input 
                type="text"
                placeholder="add an RFID tag"
                className="form-control"
                style={{marginRight: '5px'}}
                onChange={event => this.setState({rfid: event.target.value})}
                />
                <button
                    className="btn btn-success"
                    type= "button"
                    onClick={this.addPatient()}
                >Submit</button>
            </div>

            </div>
        )
    }

}

export default AddPatient;