import React, {Component} from 'react';
import Table from 'react-bootstrap/Table';

class PatientItem extends Component {
    render() {
        //console.log('this.props.patient', this.props.patients)
        const {PID, RN, Risk} = this.props.patient;
        return(
            <Table  width="600px" >
                <td width="200px">Patient ID: <strong>{PID}</strong></td>
                <td width="200px"> Room Number <strong>{RN}</strong></td>
                <td width="200px"> Risk Level: <strong>{Risk}</strong></td>
            </Table>
        )
    }
}

export default PatientItem;