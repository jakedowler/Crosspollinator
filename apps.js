APPS = [
  {
    "date": "2026-03-08",
    "word_a": "bunn",
    "word_b": "beseem",
    "name": "Bun Propriety \u2014 Does This Bun Beseem the Occasion?",
    "desc": "Does this bun beseem the occasion? You be the judge.",
    "path": "output/2026-03-08/bunn_beseem.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "bunn",
    "word_b": "beseem",
    "name": "Bun Propriety \u2014 Does This Bun Beseem the Occasion?",
    "desc": "",
    "path": "output/2026-03-08/bunn_beseem_v2.html",
    "version": 2
  },
  {
    "date": "2026-03-08",
    "word_a": "chimpanzee",
    "word_b": "ketchup",
    "name": "Ketchup Kingdom",
    "desc": "",
    "path": "output/2026-03-08/chimpanzee_ketchup.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "climb",
    "word_b": "wildfire",
    "name": "Firebreak",
    "desc": "climb x wildfire",
    "path": "output/2026-03-08/climb_wildfire.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "jewel",
    "word_b": "shelter",
    "name": "Gem Vault",
    "desc": "Place mirror panels to guide light beams to the central jewel",
    "path": "output/2026-03-08/jewel_shelter.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "llama",
    "word_b": "rowboat",
    "name": "Llama Crossing",
    "desc": "Row your rowboat to ferry all 6 llamas across the river!\n    Dodge rocks &amp; logs (they cost HP). Tap floating cargo for bonus points.\n    Use arrow buttons or A/D keys. LOAD at left bank, DOCK at right bank.",
    "path": "output/2026-03-08/llama_rowboat.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "llama",
    "word_b": "rowboat",
    "name": "Llama Crossing v2",
    "desc": "Ferry 8 unique llamas across the river!\n    Each llama has a personality that changes the ride.\n    Manage stamina, dodge hazards, pick your lane, and watch the weather.",
    "path": "output/2026-03-08/llama_rowboat_v2.html",
    "version": 2
  },
  {
    "date": "2026-03-08",
    "word_a": "radio",
    "word_b": "tale",
    "name": "Frequency",
    "desc": "radio &times; tale &mdash; tune the dial, find the story",
    "path": "output/2026-03-08/radio_tale.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "radio",
    "word_b": "tale",
    "name": "Frequency",
    "desc": "radio &times; tale &mdash; tune stations, choose your story",
    "path": "output/2026-03-08/radio_tale_v2.html",
    "version": 2
  },
  {
    "date": "2026-03-08",
    "word_a": "rollercoaster",
    "word_b": "adjust",
    "name": "Track Tuner",
    "desc": "Shape the rollercoaster track so riders get thrills without danger!",
    "path": "output/2026-03-08/rollercoaster_adjust.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "tubing",
    "word_b": "microphone",
    "name": "Tube Tones",
    "desc": "${match}% match &mdash; +${pts} pts",
    "path": "output/2026-03-08/tubing_microphone.html",
    "version": 1
  },
  {
    "date": "2026-03-08",
    "word_a": "tubing",
    "word_b": "microphone",
    "name": "Tube Tones \u2014 Sound Routing Puzzle",
    "desc": "`;\n  } else if (type === 'tee') {\n    paths = `\n             \n             \n             `;\n  } else { // cross\n    paths = `\n             \n             \n             `;\n  }\n  return `${paths}`;\n}\n\n// \u2500\u2500\u2500 LEVELS \u2500\u2500\u2500\n// Each level: {rows, cols, mics:[{r,c,note,dir}], speakers:[{r,c,note,dir}], blocked:[[r,c],...], palette:{type:count,...}, par}\n// dir = direction the sound exits/enters (0=up,1=right,2=down,3=left)\nconst LEVELS = [\n  // Level 1: Simple straight path\n  { rows:3, cols:5,\n    mics:[{r:1,c:0,note:'C',dir:1}],\n    speakers:[{r:1,c:4,note:'C',dir:3}],\n    blocked:[],\n    palette:{straight:3},\n    par:3\n  },\n  // Level 2: One bend needed\n  { rows:4, cols:4,\n    mics:[{r:0,c:1,note:'E',dir:2}],\n    speakers:[{r:2,c:3,note:'E',dir:3}],\n    blocked:[[1,2],[1,3]],\n    palette:{straight:2,bend:2},\n    par:4\n  },\n  // Level 3: Two mics, two speakers, crossing paths\n  { rows:4, cols:5,\n    mics:[{r:0,c:1,note:'C',dir:2},{r:3,c:0,note:'G',dir:1}],\n    speakers:[{r:0,c:4,note:'G',dir:3},{r:3,c:3,note:'C',dir:3}],\n    blocked:[[1,0],[2,4]],\n    palette:{straight:4,bend:3},\n    par:6\n  },\n  // Level 4: T-junction puzzle\n  { rows:4, cols:5,\n    mics:[{r:0,c:2,note:'A',dir:2}],\n    speakers:[{r:3,c:0,note:'A',dir:0},{r:3,c:4,note:'A',dir:0}],\n    blocked:[[1,0],[1,4],[2,1],[2,3]],\n    palette:{straight:3,bend:2,tee:1},\n    par:5\n  },\n  // Level 5: Multi-note routing\n  { rows:5, cols:5,\n    mics:[{r:0,c:0,note:'C',dir:2},{r:0,c:4,note:'E',dir:2},{r:4,c:0,note:'G',dir:1}],\n    speakers:[{r:4,c:4,note:'C',dir:3},{r:2,c:2,note:'E',dir:0},{r:4,c:2,note:'G',dir:0}],\n    blocked:[[1,1],[3,3],[1,3],[3,1]],\n    palette:{straight:5,bend:4,tee:1},\n    par:8\n  },\n  // Level 6: Complex routing with cross\n  { rows:5, cols:6,\n    mics:[{r:0,c:0,note:'C',dir:2},{r:0,c:5,note:'E',dir:2},{r:4,c:0,note:'G',dir:1},{r:2,c:5,note:'A',dir:3}],\n    speakers:[{r:4,c:5,note:'C',dir:0},{r:4,c:3,note:'E',dir:0},{r:0,c:3,note:'G',dir:2},{r:2,c:0,note:'A',dir:1}],\n    blocked:[[1,2],[3,4],[1,4],[3,1]],\n    palette:{straight:6,bend:5,tee:2,cross:1},\n    par:10\n  }\n];\n\n// \u2500\u2500\u2500 STATE \u2500\u2500\u2500\nlet currentLevel = 0;\nlet grid = []; // grid[r][c] = null | {type, rotation} | 'mic' | 'speaker' | 'blocked'\nlet selectedPalette = null; // {type, rotation}\nlet selectedRotation = 0;\nlet moves = 0;\nlet totalScore = 0;\nlet audioCtx = null;\nlet animFrame = 0;\nlet activeFlows = []; // for wave animation\nlet levelData = null;\n\nconst $ = s => document.querySelector(s);\nconst $$ = s => document.querySelectorAll(s);\n\n// \u2500\u2500\u2500 AUDIO \u2500\u2500\u2500\nfunction initAudio() {\n  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();\n  if (audioCtx.state === 'suspended') audioCtx.resume();\n}\n\nfunction playNote(note, duration, delay) {\n  if (!audioCtx) return;\n  const freq = FREQS[note];\n  if (!freq) return;\n  const t = audioCtx.currentTime + (delay || 0);\n  const osc = audioCtx.createOscillator();\n  const gain = audioCtx.createGain();\n  osc.type = 'triangle';\n  osc.frequency.setValueAtTime(freq, t);\n  gain.gain.setValueAtTime(0.15, t);\n  gain.gain.exponentialRampToValueAtTime(0.001, t + duration);\n  osc.connect(gain);\n  gain.connect(audioCtx.destination);\n  osc.start(t);\n  osc.stop(t + duration);\n}\n\nfunction playSuccess() {\n  if (!audioCtx) return;\n  [523.25, 659.25, 783.99, 1046.5].forEach((f, i) => {\n    const t = audioCtx.currentTime + i * 0.1;\n    const osc = audioCtx.createOscillator();\n    const gain = audioCtx.createGain();\n    osc.type = 'sine';\n    osc.frequency.setValueAtTime(f, t);\n    gain.gain.setValueAtTime(0.12, t);\n    gain.gain.exponentialRampToValueAtTime(0.001, t + 0.4);\n    osc.connect(gain);\n    gain.connect(audioCtx.destination);\n    osc.start(t);\n    osc.stop(t + 0.4);\n  });\n}\n\nfunction playFail() {\n  if (!audioCtx) return;\n  const t = audioCtx.currentTime;\n  const osc = audioCtx.createOscillator();\n  const gain = audioCtx.createGain();\n  osc.type = 'sawtooth';\n  osc.frequency.setValueAtTime(150, t);\n  osc.frequency.exponentialRampToValueAtTime(80, t + 0.3);\n  gain.gain.setValueAtTime(0.08, t);\n  gain.gain.exponentialRampToValueAtTime(0.001, t + 0.3);\n  osc.connect(gain);\n  gain.connect(audioCtx.destination);\n  osc.start(t);\n  osc.stop(t + 0.3);\n}\n\nfunction playPlace() {\n  if (!audioCtx) return;\n  const t = audioCtx.currentTime;\n  const osc = audioCtx.createOscillator();\n  const gain = audioCtx.createGain();\n  osc.type = 'sine';\n  osc.frequency.setValueAtTime(600, t);\n  osc.frequency.exponentialRampToValueAtTime(900, t + 0.08);\n  gain.gain.setValueAtTime(0.06, t);\n  gain.gain.exponentialRampToValueAtTime(0.001, t + 0.1);\n  osc.connect(gain);\n  gain.connect(audioCtx.destination);\n  osc.start(t);\n  osc.stop(t + 0.1);\n}\n\nfunction playRemove() {\n  if (!audioCtx) return;\n  const t = audioCtx.currentTime;\n  const osc = audioCtx.createOscillator();\n  const gain = audioCtx.createGain();\n  osc.type = 'sine';\n  osc.frequency.setValueAtTime(500, t);\n  osc.frequency.exponentialRampToValueAtTime(300, t + 0.08);\n  gain.gain.setValueAtTime(0.05, t);\n  gain.gain.exponentialRampToValueAtTime(0.001, t + 0.1);\n  osc.connect(gain);\n  gain.connect(audioCtx.destination);\n  osc.start(t);\n  osc.stop(t + 0.1);\n}\n\n// \u2500\u2500\u2500 TUBE CONNECTION LOGIC \u2500\u2500\u2500\nfunction getConnections(type, rotation) {\n  // Returns array of direction indices this tube connects\n  const base = CONNECTIONS[type];\n  const dirs = new Set();\n  for (const group of base) {\n    for (const d of group) {\n      dirs.add((d + rotation) % 4);\n    }\n  }\n  return [...dirs];\n}\n\nfunction canConnect(type, rotation, fromDir) {\n  // Check if a tube of this type/rotation accepts connection from direction fromDir\n  // fromDir is the direction we're COMING FROM (so we need to check if the tube has the opposite direction)\n  const needed = OPPOSITE[fromDir];\n  return getConnections(type, rotation).includes(fromDir);\n}\n\n// \u2500\u2500\u2500 PATH FINDING \u2500\u2500\u2500\n// BFS from each mic, following tube connections, return which speakers each mic reaches\nfunction traceAllPaths() {\n  const lvl = levelData;\n  const results = []; // [{mic, reachedSpeakers:[{r,c,note}], path:[[r,c],...]}]\n\n  for (const mic of lvl.mics) {\n    const visited = new Set();\n    const queue = [{r: mic.r, c: mic.c, fromDir: -1}];\n    const path = [];\n    const reached = [];\n\n    // The mic outputs in direction mic.dir\n    // So we start by moving in that direction\n    const startR = mic.r + DIR_DR[mic.dir][0];\n    const startC = mic.c + DIR_DR[mic.dir][1];\n\n    if (startR = lvl.rows || startC = lvl.cols) {\n      results.push({mic, reached:[], path:[]});\n      continue;\n    }\n\n    const bfsQueue = [{r: startR, c: startC, enterDir: OPPOSITE[mic.dir]}];\n    const visitedKey = (r,c) => `${r},${c}`;\n    const visitedSet = new Set();\n    visitedSet.add(visitedKey(mic.r, mic.c));\n    const pathCells = [[mic.r, mic.c]];\n\n    while (bfsQueue.length > 0) {\n      const {r, c, enterDir} = bfsQueue.shift();\n      const key = visitedKey(r, c);\n      if (visitedSet.has(key)) continue;\n      visitedSet.add(key);\n\n      // Check if this is a speaker\n      const spk = lvl.speakers.find(s => s.r === r && s.c === c);\n      if (spk) {\n        // Check if we're entering from the right direction\n        if (enterDir === spk.dir) {\n          reached.push(spk);\n          pathCells.push([r, c]);\n        }\n        continue; // Don't go through speakers\n      }\n\n      // Check if there's a tube here\n      const cell = grid[r] && grid[r][c];\n      if (!cell || typeof cell !== 'object' || !cell.type) continue;\n\n      // Check if this tube accepts the entering direction\n      const conns = getConnections(cell.type, cell.rotation);\n      if (!conns.includes(enterDir)) continue;\n\n      pathCells.push([r, c]);\n\n      // Follow all OTHER connections (not the one we entered from)\n      for (const dir of conns) {\n        if (dir === enterDir) continue; // don't go back\n        const nr = r + DIR_DR[dir][0];\n        const nc = c + DIR_DR[dir][1];\n        if (nr >= 0 && nr = 0 && nc  m.r === r && m.c === c);\n      if (mic) {\n        cell.classList.add('mic');\n        cell.innerHTML = `\ud83c\udf99\ufe0f${mic.note}`;\n        // Add direction indicator\n        cell.title = `Mic: ${mic.note} (outputs ${['up','right','down','left'][mic.dir]})`;\n        addDirectionIndicator(cell, mic.dir, 'var(--mic)');\n      }\n      // Check if speaker\n      else if (lvl.speakers.find(s => s.r === r && s.c === c)) {\n        const spk = lvl.speakers.find(s => s.r === r && s.c === c);\n        cell.classList.add('speaker');\n        cell.innerHTML = `\ud83d\udd0a${spk.note}`;\n        cell.title = `Speaker: wants ${spk.note} (receives from ${['up','right','down','left'][spk.dir]})`;\n        addDirectionIndicator(cell, spk.dir, 'var(--speaker)');\n      }\n      // Check if blocked\n      else if (lvl.blocked.some(b => b[0] === r && b[1] === c)) {\n        cell.classList.add('empty');\n        cell.style.background = 'rgba(255,255,255,0.01)';\n        cell.innerHTML = '\u2715';\n      }\n      // Placeable cell\n      else {\n        const tubeData = grid[r][c];\n        if (tubeData && typeof tubeData === 'object') {\n          cell.classList.add('tube', 'placed');\n          cell.innerHTML = `${tubeSVG(tubeData.type, tubeData.rotation)}`;\n        } else {\n          cell.classList.add('tube');\n        }\n        cell.addEventListener('click', () => onCellClick(r, c));\n      }\n\n      gridEl.appendChild(cell);\n    }\n  }\n}\n\nfunction addDirectionIndicator(cell, dir, color) {\n  const arrow = document.createElement('div');\n  arrow.style.cssText = `position:absolute;font-size:10px;color:${color};opacity:0.7;`;\n  const arrows = ['\u25b2','\u25b6','\u25bc','\u25c0'];\n  arrow.textContent = arrows[dir];\n  const positions = [\n    'top:0;left:50%;transform:translateX(-50%)',\n    'right:1px;top:50%;transform:translateY(-50%)',\n    'bottom:0;left:50%;transform:translateX(-50%)',\n    'left:1px;top:50%;transform:translateY(-50%)'\n  ];\n  arrow.style.cssText += positions[dir];\n  cell.appendChild(arrow);\n}\n\n// \u2500\u2500\u2500 PALETTE RENDERING \u2500\u2500\u2500\nfunction renderPalette() {\n  const lvl = levelData;\n  const pal = $('#palette');\n  pal.innerHTML = '';\n\n  // Count how many of each type are already placed\n  const placed = {};\n  for (let r = 0; r ${tubeSVG(type, selectedPalette && selectedPalette.type === type ? selectedRotation : 0)}`;\n\n    if (remaining > 0) {\n      const countBadge = document.createElement('div');\n      countBadge.className = 'pal-count';\n      countBadge.textContent = remaining;\n      item.appendChild(countBadge);\n    }\n\n    item.addEventListener('click', (e) => {\n      e.stopPropagation();\n      initAudio();\n      if (selectedPalette && selectedPalette.type === type) {\n        // Rotate\n        selectedRotation = (selectedRotation + 1) % 4;\n        playPlace();\n      } else {\n        if (remaining  {\n  const cell = e.target.closest('.cell.placed');\n  if (!cell) return;\n  e.preventDefault();\n  const r = +cell.dataset.r;\n  const c = +cell.dataset.c;\n  grid[r][c] = null;\n  playRemove();\n  renderGrid();\n  renderPalette();\n});\n\n// Long press for mobile removal\nlet longPressTimer = null;\ndocument.addEventListener('touchstart', (e) => {\n  const cell = e.target.closest('.cell.placed');\n  if (!cell) return;\n  longPressTimer = setTimeout(() => {\n    const r = +cell.dataset.r;\n    const c = +cell.dataset.c;\n    grid[r][c] = null;\n    playRemove();\n    renderGrid();\n    renderPalette();\n  }, 500);\n});\ndocument.addEventListener('touchend', () => { clearTimeout(longPressTimer); });\ndocument.addEventListener('touchmove', () => { clearTimeout(longPressTimer); });\n\n// \u2500\u2500\u2500 CLEAR \u2500\u2500\u2500\n$('#clear-btn').addEventListener('click', () => {\n  initAudio();\n  playRemove();\n  const lvl = levelData;\n  for (let r = 0; r  {\n  initAudio();\n  const results = traceAllPaths();\n  const lvl = levelData;\n\n  // Animate flow\n  animateFlow(results);\n\n  // Check if all speakers are reached with correct notes\n  let allCorrect = true;\n  let correctCount = 0;\n  const speakersReached = new Set();\n\n  for (const res of results) {\n    for (const spk of res.reached) {\n      speakersReached.add(`${spk.r},${spk.c}`);\n      if (spk.note === res.mic.note) {\n        correctCount++;\n        // Play the note with delay for satisfaction\n        playNote(spk.note, 0.4, correctCount * 0.15);\n      } else {\n        allCorrect = false;\n        // Wrong note sound\n        setTimeout(() => playFail(), correctCount * 150 + 100);\n      }\n    }\n  }\n\n  // Check if all speakers are reached\n  if (speakersReached.size  {\n      playSuccess();\n      const par = lvl.par;\n      const stars = moves  {\n      const reached = speakersReached.size;\n      const total = lvl.speakers.length;\n      showFloatText($('#check-btn'), `${reached}/${total} speakers`, reached > 0 ? 'var(--gold)' : 'var(--accent)');\n    }, 400);\n  }\n});\n\n// \u2500\u2500\u2500 FLOW ANIMATION \u2500\u2500\u2500\nfunction animateFlow(results) {\n  const gridEl = $('#grid');\n  const rect = gridEl.getBoundingClientRect();\n  const lvl = levelData;\n  const cellSize = rect.width / lvl.cols;\n\n  // Remove old particles\n  document.querySelectorAll('.flow-particle').forEach(p => p.remove());\n\n  activeFlows = [];\n\n  for (const res of results) {\n    if (res.path.length  s.note === res.mic.note);\n    const color = isCorrect ? 'var(--teal)' : 'var(--accent)';\n\n    for (let i = 0; i  {\n        const [pr, pc] = res.path[i];\n        const particle = document.createElement('div');\n        particle.className = 'flow-particle';\n        particle.style.background = color;\n        particle.style.boxShadow = `0 0 8px ${color}`;\n        particle.style.left = (rect.left + pc * cellSize + cellSize/2 - 3) + 'px';\n        particle.style.top = (rect.top + pr * cellSize + cellSize/2 - 3) + 'px';\n        particle.style.transition = 'opacity 0.4s';\n        document.body.appendChild(particle);\n\n        // Highlight cell\n        const cellEl = gridEl.children[pr * lvl.cols + pc];\n        if (cellEl) {\n          cellEl.classList.add('connected');\n          cellEl.style.boxShadow = `0 0 12px ${color}`;\n          setTimeout(() => {\n            cellEl.classList.remove('connected');\n            cellEl.style.boxShadow = '';\n          }, 600);\n        }\n\n        setTimeout(() => {\n          particle.style.opacity = '0';\n          setTimeout(() => particle.remove(), 400);\n        }, 300);\n      }, i * 120);\n    }\n  }\n}\n\nfunction showFloatText(anchor, text, color) {\n  const rect = anchor.getBoundingClientRect();\n  const el = document.createElement('div');\n  el.className = 'float-text';\n  el.textContent = text;\n  el.style.color = color;\n  el.style.left = rect.left + rect.width/2 - 40 + 'px';\n  el.style.top = rect.top - 20 + 'px';\n  el.style.fontSize = '14px';\n  document.body.appendChild(el);\n  setTimeout(() => el.remove(), 800);\n}\n\n// \u2500\u2500\u2500 WAVE CANVAS ANIMATION \u2500\u2500\u2500\nfunction drawWave() {\n  const canvas = $('#wave-canvas');\n  if (!canvas) return;\n  const ctx = canvas.getContext('2d');\n  const dpr = window.devicePixelRatio || 1;\n  const W = canvas.width = canvas.clientWidth * dpr;\n  const H = canvas.height = canvas.clientHeight * dpr;\n  ctx.clearRect(0, 0, W, H);\n\n  if (!levelData) return;\n  const lvl = levelData;\n  const mid = H / 2;\n  const amp = H * 0.35;\n\n  // Draw target waveform based on mic notes\n  ctx.lineWidth = 1.5 * dpr;\n  for (let mi = 0; mi = LEVELS.length - 1;\n\n  box.innerHTML = `\n    Level ${currentLevel + 1} Complete!\n    ${starsStr}\n    ${parText} (${moves} moves, par ${levelData.par})",
    "path": "output/2026-03-08/tubing_microphone_v2.html",
    "version": 2
  },
  {
    "date": "2026-03-09",
    "word_a": "paprika",
    "word_b": "afford",
    "name": "YIELD \u2014 Spice Market Game",
    "desc": "Best: Round ${bestRound + 1} &mdash; ${bestResult.totalFlavor} flavor (target ${TARGET})",
    "path": "output/2026-03-09/paprika_afford.html",
    "version": 1
  }
];
