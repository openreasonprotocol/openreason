import { CheckCircle, AlertTriangle, TrendingDown } from 'lucide-react'

export const Check = () => (
  <CheckCircle
    width={18}
    height={18}
    style={{
      display: 'inline',
      marginRight: '4px',
      color: '#10b981',
      verticalAlign: 'text-bottom'
    }}
  />
)

export const Warning = () => (
  <AlertTriangle
    width={18}
    height={18}
    style={{
      display: 'inline',
      marginRight: '4px',
      color: '#f59e0b',
      verticalAlign: 'text-bottom'
    }}
  />
)

export const Cheaper = () => (
  <TrendingDown
    width={18}
    height={18}
    style={{
      display: 'inline',
      marginRight: '4px',
      color: '#10b981',
      verticalAlign: 'text-bottom'
    }}
  />
)

export const CheckSmall = () => (
  <CheckCircle
    width={16}
    height={16}
    style={{
      display: 'inline',
      color: '#10b981',
      verticalAlign: 'text-bottom'
    }}
  />
)

export const WarningSmall = () => (
  <AlertTriangle
    width={16}
    height={16}
    style={{
      display: 'inline',
      color: '#f59e0b',
      verticalAlign: 'text-bottom'
    }}
  />
)
