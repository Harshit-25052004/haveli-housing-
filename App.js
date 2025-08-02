import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';


import Navbar from './components/navbar';
import HeroSection from './components/HeroSection';
import FeaturedCarousel from './components/FeaturedCarousel';
import ListProperty from "./components/ListProperty";
import LoginModal from "./components/LoginModal";
import { AuthProvider } from "./context/AuthContext";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();
function App() {
  
  return (
        <QueryClientProvider client={queryClient}>
      <AuthProvider>
    <BrowserRouter>
  
      <Routes>
        <Route path="/login" element={<LoginModal />} />
      
        <Route path="/" element={
          <>
          <Navbar />
            <HeroSection />
            <FeaturedCarousel />
          </>
        } />
         
        <Route path="/list-property" element={<ListProperty />} />
      </Routes>

    </BrowserRouter>
    </AuthProvider>
    </QueryClientProvider >
  );
}

export default App;

