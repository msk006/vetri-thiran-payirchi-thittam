const task = document.getElementById('task');
const inputText = document.getElementById('inputText');
const inputLabel = document.getElementById('inputLabel');
const level = document.getElementById('level');
const weeksWrap = document.getElementById('weeksWrap');
const countWrap = document.getElementById('countWrap');
const weeks = document.getElementById('weeks');
const count = document.getElementById('count');
const submitBtn = document.getElementById('submitBtn');
const result = document.getElementById('result');
const status = document.getElementById('status');
const copyBtn = document.getElementById('copyBtn');

const placeholders = {
  qa: ['Your question', 'Example: What is the largest ocean?'],
  explain: ['Topic to explain', 'Example: Explain the Pythagoras theorem simply.'],
  quiz: ['Topic or passage', 'Paste a lesson, paragraph, or topic here.'],
  summarize: ['Passage to summarize', 'Paste your educational notes here.'],
  learn: ['Topic to learn', 'Example: SQL for a beginner computer science student.']
};

function updateUI() {
  const type = task.value;
  inputLabel.textContent = placeholders[type][0];
  inputText.placeholder = placeholders[type][1];
  weeksWrap.classList.toggle('hidden', type !== 'learn');
  countWrap.classList.toggle('hidden', type !== 'quiz');
  level.parentElement.classList.toggle('hidden', type !== 'explain' && type !== 'learn');
}

task.addEventListener('change', updateUI);
updateUI();

function renderQuiz(data) {
  return data.questions.map((q, i) => `
    <div class="quiz-question">
      <strong>${i + 1}. ${escapeHtml(q.question)}</strong>
      ${q.options.map(o => `<div class="quiz-option">${escapeHtml(o)}</div>`).join('')}
      <div class="quiz-answer">Answer: ${escapeHtml(q.answer)}</div>
      ${q.explanation ? `<div>${escapeHtml(q.explanation)}</div>` : ''}
    </div>
  `).join('');
}

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
}

submitBtn.addEventListener('click', async () => {
  const text = inputText.value.trim();
  if (!text) return;

  const type = task.value;
  const endpoint = {
    qa: '/qa', explain: '/explain', quiz: '/quiz', summarize: '/summarize', learn: '/learn/recommendations'
  }[type];
  const body = { text };
  if (type === 'explain' || type === 'learn') body.level = level.value;
  if (type === 'learn') body.weeks = Number(weeks.value);
  if (type === 'quiz') body.count = Number(count.value);

  submitBtn.disabled = true;
  copyBtn.disabled = true;
  status.textContent = 'Thinking…';
  result.className = 'result muted';
  result.textContent = 'EduGenie is generating your result…';

  try {
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || 'Request failed');

    result.className = 'result';
    if (type === 'quiz') {
      result.innerHTML = renderQuiz(data);
    } else {
      result.textContent = data.result;
    }
    copyBtn.disabled = false;
    status.textContent = 'Done';
  } catch (error) {
    result.className = 'result muted';
    result.textContent = `Error: ${error.message}`;
    status.textContent = 'Error';
  } finally {
    submitBtn.disabled = false;
  }
});

copyBtn.addEventListener('click', async () => {
  const text = result.innerText;
  await navigator.clipboard.writeText(text);
  status.textContent = 'Copied';
  setTimeout(() => status.textContent = 'Ready', 1200);
});
