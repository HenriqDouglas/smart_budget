// src/App.tsx
import { Container, Typography, Button } from "@mui/material";

function App() {
  return (
    <Container maxWidth="sm" sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Despesas Inteligente
      </Typography>
      <Button variant="contained" color="primary">
        Testar MUI
      </Button>
    </Container>
  );
}

export default App;
