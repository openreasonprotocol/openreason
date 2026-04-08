import { Rocket, FileText, Wrench, BookOpen, Users, BarChart3 } from 'lucide-react'

export default {
  "index": "Overview",
  "---getting-started": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Rocket size={16} style={{ color: '#0066cc' }} />
        <span>Getting Started</span>
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
        <FileText size={16} style={{ color: '#0066cc' }} />
        <span>Protocol</span>
      </div>
    )
  },
  "protocol": {
    "display": "children"
  },
  "---tools": {
    "type": "separator",
    "title": (
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <Wrench size={16} style={{ color: '#0066cc' }} />
        <span>Tools</span>
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
        <BarChart3 size={16} style={{ color: '#0066cc' }} />
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
        <BookOpen size={16} style={{ color: '#0066cc' }} />
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
        <Users size={16} style={{ color: '#0066cc' }} />
        <span>Community</span>
      </div>
    )
  },
  "community": {
    "display": "children"
  }
}
