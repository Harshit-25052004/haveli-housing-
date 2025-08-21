// Mock database for properties
export const properties = [
  {
    _id: "68864aa2a3c55c813f55dc51",
    name: "VRB Sparkle",
    rera_number: "RAJ2025VS002",
    address: {
      // Address object structure - you can expand this as needed
      city: "Jaipur",
      area: "Tonk Road"
    },
    specification: "Luxury Modern Community",
    rate: 2800,
    total_plots: 85,
    ////img: "vrb_sparkle.jpg",
    description: "Luxury plotted development with wide roads, green zones, and proximity to key locations",
    map_url: "https://maps.google.com/?q=VRB+Sparkle+Tonk+Road+Jaipur"
  },
  {
    _id: "68864aa2a3c55c813f55dc52",
    name: "VRB Sapphire Park",
    rera_number: "RAJ2025VSP003",
    address: {
      city: "Jaipur",
      area: "Kalwar Road"
    },
    specification: "Modern Vastu-Compliant Layout",
    rate: 3000,
    total_plots: 95,
    //img: "vrb_sapphire_park.jpg",
    description: "A modern gated community with well-laid roads and eco-friendly planning",
    map_url: "https://maps.google.com/?q=VRB+Sapphire+Park+Kalwar+Road+Jaipur"
  },
  {
    _id: "68864aa2a3c55c813f55dc53",
    name: "Elite Word Dreamworld City",
    rera_number: "RAJ2025EDC004",
    address: {
      city: "Jaipur",
      area: "Jagatpura"
    },
    specification: "Smart Investment Destination",
    rate: 3200,
    total_plots: 150,
    //img: "elite_dreamworld.jpg",
    description: "Smart city plots with premium amenities, future metro connectivity, and modern infrastructure",
    map_url: "https://maps.google.com/?q=Elite+Dreamworld+City+Jagatpura+Jaipur"
  },
  {
    _id: "68864aa2a3c55c813f55dc54",
    name: "VRB World City",
    rera_number: "RAJ2025VWC005",
    address: {
      city: "Jaipur",
      area: "Sikar Road"
    },
    specification: "Affordable Family Housing",
    rate: 2700,
    total_plots: 110,
    //img: "vrb_world_city.jpg",
    description: "Affordable residential plots with high-growth potential due to proximity to major highways",
    map_url: "https://maps.google.com/?q=VRB+World+City+Sikar+Road+Jaipur"
  },
  {
    _id: "68864aa2a3c55c813f55dc55",
    name: "Ring Avenue Ring Enclave",
    rera_number: "RAJ2025RARE006",
    address: {
      city: "Jaipur",
      area: "Ring Road"
    },
    specification: "Eco-Friendly Green Living",
    rate: 2600,
    total_plots: 100,
    //img: "ring_avenue_enclave.jpg",
    description: "Strategically located project with seamless ring road access and lush green environment",
    map_url: "https://maps.google.com/?q=Ring+Avenue+Enclave+Ring+Road+Jaipur"
  }
];

// Helper function to get property images
/*export const getPropertyImage = (imageName) => {
  // For now, using placeholder images from Unsplash
  // In a real app, these would be stored images
  const imageMap = {
    "vrb_sparkle.jpg": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "vrb_sapphire_park.jpg": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "elite_dreamworld.jpg": "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "vrb_world_city.jpg": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "ring_avenue_enclave.jpg": "https://images.unsplash.com/photo-1600573472591-ee6b68d14c68?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
  };
  
  return imageMap[imageName] || "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80";
};*/
