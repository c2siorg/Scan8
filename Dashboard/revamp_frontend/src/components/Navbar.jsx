import { Navbar, Container, Button }from 'react-bootstrap';

const NavBar = ({modal,setModal}) =>{
    return(
        <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand className="fs-2 fw-bold">Scan8</Navbar.Brand>
          <Button className="fw-bold" variant="outline-success" onClick={() => setModal(!modal)}>New Scan</Button>
        </Container>
      </Navbar>
    );
}

export default NavBar;
