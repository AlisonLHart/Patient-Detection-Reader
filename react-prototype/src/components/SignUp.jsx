import React, {Component} from 'react'; 

class SignUp extends Component{ // So react is handy dandy in that it's super object oriented. Components are basically objects
    //https://reactjs.org/docs/components-and-props.html
    constructor(props) {
        super(props)
        this.state = {
            email: '',
            password: ''
        }
    }
    
    //helper method
    signUp(){
        console.log('this.state', this.state)
    }

    render() {
        //wow, look at this nonsense
        //This is the sign in page
        return(
            <div className="form-inline">
                <h2>Sign Up</h2>
                <div className="form-group">
                    <input
                        className="form-control"
                        type ="text"
                        placeholder="email"
                        onChange={event => this.setState({email: event.target.value})}
                        />
                    <input
                        className="form-control"
                        type ="password"
                        placeholder="password"
                        onChange={event => this.setState({password: event.target.value})}
                        />
                    <button
                        className="btn btn-primary"
                        type = "button"
                        onClick={() => this.signUp()}>
                    Sign Up
                    </button>
                </div>
                </div>
        )
    }
}

export default SignUp;