import { Rocket, FileText, Boxes, Wrench, BookOpen, Users, BarChart3 } from 'lucide-react'

export default {
  "index": "Home",
  "story": { "display": "hidden" },
  "embed": { "display": "hidden" },
  "what-it-is": { "display": "hidden" },
  "how-it-works": { "display": "hidden" },
  "about": { "display": "hidden" },
  "---getting-started": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Rocket size={16} style={{ color: '#FF5D2A' }} />
        <span>Start here</span>
      </div>
    )
  },
  "getting-started": {
    "display": "children"
  },
  "---protocol": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <FileText size={16} style={{ color: '#FF5D2A' }} />
        <span>Concepts</span>
      </div>
    )
  },
  "protocol": {
    "display": "children"
  },
  "---data-products": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Boxes size={16} style={{ color: '#FF5D2A' }} />
        <span>Data Products</span>
      </div>
    )
  },
  "data-products": {
    "display": "children"
  },
  "---tools": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Wrench size={16} style={{ color: '#FF5D2A' }} />
        <span>Reference</span>
      </div>
    )
  },
  "tools": {
    "display": "children"
  },
  "---analysis": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <BarChart3 size={16} style={{ color: '#FF5D2A' }} />
        <span>Analysis</span>
      </div>
    )
  },
  "analysis": {
    "display": "children"
  },
  "---examples": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <BookOpen size={16} style={{ color: '#FF5D2A' }} />
        <span>Examples</span>
      </div>
    )
  },
  "examples": {
    "display": "children"
  },
  "---community": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Users size={16} style={{ color: '#FF5D2A' }} />
        <span>Community</span>
      </div>
    )
  },
  "community": {
    "display": "children"
  }
}
