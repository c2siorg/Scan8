import { Navbar, Container, Button }from 'react-bootstrap';

const NavBar = () =>{
    return(
        <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand className="fs-2 fw-bold">Scan8</Navbar.Brand>
          <Button className="fw-bold" variant="outline-success">New Scan</Button>
        </Container>
      </Navbar>
    );
}

export default NavBar;
