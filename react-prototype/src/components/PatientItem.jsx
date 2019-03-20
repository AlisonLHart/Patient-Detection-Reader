import React, {Component} from 'react';

class PatientItem extends Component {
    render() {
        console.log('this.props.patient', this.props.patients)
        return(
            <div>I'm a sexy seahorse</div>
        )
    }
}

export default PatientItem;