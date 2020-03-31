# Signal Analysis

scipy API <http://scipy.github.io/devdocs/api.html#api-definition>

- Image <http://scipy.github.io/devdocs/ndimage.html#module-scipy.ndimage>
- Waveforms <http://scipy.github.io/devdocs/signal.html#module-scipy.signal>
  - chirp(t, f0, t1, f1[, method, phi, vertex_zero])
    - Frequency-swept cosine generator.
  - gausspulse(t[, fc, bw, bwr, tpr, retquad, ...])
    - Return a Gaussian modulated sinusoid:
  - sawtooth(t[, width])
    - Return a periodic sawtooth or triangle waveform.
  - square(t[, duty])
    - Return a periodic square-wave waveform.
  - sweep_poly(t, poly[, phi])
    - Frequency-swept cosine generator, with a time-dependent frequency.
