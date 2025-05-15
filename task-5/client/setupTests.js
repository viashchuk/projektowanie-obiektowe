import '@testing-library/jest-dom'
import { TextEncoder, TextDecoder } from 'util'

if (!global.TextEncoder) {
  global.TextEncoder = TextEncoder
}

if (!global.TextDecoder) {
  global.TextDecoder = TextDecoder
}