<template>
    <div class="about_page">
      <div class="top1-title">
        <h1>智慧教育系统</h1>
        <span>实现教学质量的飞跃</span>
      </div>
      <div class="top1-introduction">
        <span>智慧教育系统旨在利用人工智能和现代化技术，为课堂教学提供全面的数据分析与管理工具。我们的目标是帮助教育者提升课堂效率，优化教学策略，同时为学生创造更智能、更高效的学习环境。</span>
      </div>
      <div class="top2-introduction">
        <h2>个人功能简介:</h2>
        <p>个人功能主要涵盖了四个部分，通过位于每个同学课桌前的摄像头进行分析。得到的结果有助于老师分析每位同学上课的专注情况，也便于学生了解自己在课堂上的情况的情况。</p>
        
        <div class="features">
          <div class="feature-item">
            <div class="feature-icon">
              <i class="fas fa-brain"></i>
            </div>
            <h3>专注度分析</h3>
            <p>利用姿态检测，行为统计和情绪行为的综合检测来确定学生专注于课堂的程度</p>
          </div>
          
          <div class="feature-item">
            <div class="feature-icon">
              <i class="fas fa-video"></i>
            </div>
            <h3>作弊检测</h3>
            <p>通过摄像头实时捕获违规行为，如传递纸条，交头接耳，回头，使用手机等种种作弊情况</p>
          </div>
          
          <div class="feature-item">
            <div class="feature-icon">
              <i class="fas fa-chalkboard-teacher"></i>
            </div>
            <h3>情绪分析</h3>
            <p>实时统计学生在上课时的情绪情况，佐证专注度分析，使专注度分析更加有理有据</p>
          </div>

          <div class="feature-item">
            <div class="feature-icon">
              <i class="fas fa-video"></i>
            </div>
            <h3>行为分析</h3>
            <p>统计课堂上回头，睡觉，写字，看书，玩手机的情况等，以判断学生专注于课堂的情况</p>
          </div>
        </div>
        
        <h2>群体功能简介:</h2>
        <p>群体的功能主要分两部分，行为分析和整体作弊检测，可以帮老师宏观定位是哪个学生的问题。</p>
        
        <div class="features">
          <div class="feature-item">
            <div class="feature-icon">
              <i class="fas fa-brain"></i>
            </div>
            <h3>专注度分析</h3>
            <p>利用姿态检测，行为统计和情绪行为的综合检测来确定学生专注于课堂的程度</p>
          </div>
          
          <div class="feature-item">
            <div class="feature-icon">
              <i class="fas fa-video"></i>
            </div>
            <h3>作弊检测</h3>
            <p>通过摄像头实时捕获违规行为，如传递纸条，交头接耳，回头，使用手机等种种作弊情况</p>
          </div>
        </div>


        <div class="benefits">
          <h2>我们的优势</h2>
          <div class="benefit-item">
            <div class="benefit-icon">
              <i class="fas fa-chart-line"></i>
            </div>
            <div class="benefit-content">
              <h3>检测效果卓越</h3>
              <p>训练情绪分析功能的数据集采用了闭源百万图片集AffectNet，侦测细微表情明锐，效果精良。</p>
            </div>
          </div>
          
          <div class="benefit-item">
            <div class="benefit-icon">
              <i class="fas fa-shield-alt"></i>
            </div>
            <div class="benefit-content">
              <h3>多模态观察</h3>
              <p>从多方面综合产生数据分析，最后生成一个整体的报告，对比单一分析可靠性优秀全面，效果卓越。</p>
            </div>
          </div>
          
          <div class="benefit-item">
            <div class="benefit-icon">
              <i class="fas fa-headset"></i>
            </div>
            <div class="benefit-content">
              <h3>人性化</h3>
              <p>界面清洁，操作简单，结果可视化好，上手难度低</p>
            </div>
          </div>
        </div>
        
        <div class="testimonials">
          <h2>用户评价</h2>
          <div class="testimonial-slider">
            <div class="testimonial-slide active">
              <div class="testimonial-content">
                <p>"智慧教育系统彻底改变了我们的教学方式，学生们的学习积极性明显提高，教学效果显著提升。"</p>
                <div class="testimonial-author">
                  <div class="author-info">
                    <h4>张老师</h4>
                    <span>高中数学教师</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="testimonial-slide">
              <div class="testimonial-content">
                <p>"作为一个学生，我非常喜欢这个系统，它能根据我的学习情况自动调整学习内容，让我学得更高效。"</p>
                <div class="testimonial-author">
                  <div class="author-info">
                    <h4>李同学</h4>
                    <span>高三学生</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="slider-controls">
            <button class="prev-btn">&lt;</button>
            <button class="next-btn">&gt;</button>
          </div>
        </div>
        
        <div class="contact-section">
          <h2>联系我们的团队</h2>
          <p>如果您想了解更多关于智慧教育系统的信息，或者有任何疑问，请随时联系我们</p>
          <form class="contact-form">
            <div class="form-group">
              <label for="name">姓名</label>
              <input type="text" id="name" placeholder="请输入您的姓名">
            </div>
            <div class="form-group">
              <label for="email">邮箱</label>
              <input type="email" id="email" placeholder="请输入您的邮箱">
            </div>
            <div class="form-group">
              <label for="message">留言</label>
              <textarea id="message" placeholder="请输入您的留言内容"></textarea>
            </div>
            <button type="submit" class="submit-btn">提交</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutPage',
    mounted() {
      // 初始化轮播图
      this.initSlider();
    },
    methods: {
      initSlider() {
        // 简单的轮播逻辑
        let currentSlide = 0;
        const slides = document.querySelectorAll('.testimonial-slide');
        const totalSlides = slides.length;
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        
        function showSlide(index) {
          slides.forEach(slide => slide.classList.remove('active'));
          slides[index].classList.add('active');
        }
        
        prevBtn.addEventListener('click', () => {
          currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
          showSlide(currentSlide);
        });
        
        nextBtn.addEventListener('click', () => {
          currentSlide = (currentSlide + 1) % totalSlides;
          showSlide(currentSlide);
        });
        
        // 自动轮播
        setInterval(() => {
          currentSlide = (currentSlide + 1) % totalSlides;
          showSlide(currentSlide);
        }, 5000);
      }
    }
  }
  </script>
  
  <style scoped>
  .about_page {
    display: flex;
    flex-direction: column;
    text-align: center;
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .top1-title {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 3rem;
  }
  
  .top1-title h1 {
    margin: 5px 0;
    font-size: 2.5rem;
    color: #333;
  }
  
  .top1-title span {
    font-size: 1.2rem;
    color: #666;
  }
  
  .top2-introduction {
    text-align: left;
  }
  
  .top2-introduction h2 {
    margin-bottom: 1rem;
    color: #333;
    font-size: 1.8rem;
  }
  
  .top2-introduction p {
    margin-bottom: 2rem;
    font-size: 1.1rem;
    line-height: 1.6;
    color: #555;
  }
  
  .features {
    display: flex;
    justify-content: space-between;
    margin: 3rem 0;
    flex-wrap: wrap;
  }
  
  .feature-item {
    flex: 0 0 calc(33.333% - 1.5rem);
    background-color: #fff;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }
  
  .feature-item:hover {
    transform: translateY(-5px);
  }
  
  .feature-icon {
    font-size: 2rem;
    color: #4285f4;
    margin-bottom: 1rem;
  }
  
  .feature-item h3 {
    margin-bottom: 0.5rem;
    color: #333;
  }
  
  .feature-item p {
    color: #666;
    font-size: 0.95rem;
  }
  
  .benefits {
    margin: 3rem 0;
  }
  
  .benefits h2 {
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .benefit-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 2rem;
  }
  
  .benefit-icon {
    flex: 0 0 50px;
    font-size: 1.8rem;
    color: #4285f4;
    margin-right: 1.5rem;
  }
  
  .benefit-content h3 {
    margin-bottom: 0.5rem;
    color: #333;
  }
  
  .testimonials {
    margin: 3rem 0;
  }
  
  .testimonials h2 {
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .testimonial-slider {
    position: relative;
  }
  
  .testimonial-slide {
    display: none;
    text-align: center;
  }
  
  .testimonial-slide.active {
    display: block;
  }
  
  .testimonial-content p {
    font-style: italic;
    font-size: 1.1rem;
    margin: 2rem 0;
    padding: 0 2rem;
    position: relative;
  }
  
  .testimonial-content p::before,
  .testimonial-content p::after {
    content: '"';
    font-size: 3rem;
    color: #ddd;
    position: absolute;
  }
  
  .testimonial-content p::before {
    left: 0;
    top: -1rem;
  }
  
  .testimonial-content p::after {
    right: 0;
    bottom: -2rem;
  }
  
  .testimonial-author {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .testimonial-author img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-right: 1rem;
  }
  
  .author-info h4 {
    margin-bottom: 0.2rem;
  }
  
  .author-info span {
    color: #666;
    font-size: 0.9rem;
  }
  
  .slider-controls {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
  }
  
  .slider-controls button {
    background-color: #4285f4;
    color: white;
    border: none;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin: 0 0.5rem;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
  }
  
  .slider-controls button:hover {
    background-color: #3367d6;
  }
  
  .contact-section {
    background-color: #f8f9fa;
    padding: 3rem;
    text-align: center;
    border-radius: 8px;
    margin-top: 3rem;
  }
  
  .contact-section h2 {
    margin-bottom: 1rem;
  }
  
  .contact-section p {
    margin-bottom: 2rem;
  }
  
  .contact-form {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 1.5rem;
    text-align: left;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #333;
  }
  
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
  }
  
  .form-group textarea {
    height: 150px;
    resize: vertical;
  }
  
  .submit-btn {
    background-color: #4285f4;
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .submit-btn:hover {
    background-color: #3367d6;
  }
  
  /* 响应式设计 */
  @media (max-width: 992px) {
    .features {
      flex-direction: column;
    }
    
    .feature-item {
      flex: 0 0 100%;
    }
    
    .benefit-item {
      flex-direction: column;
      text-align: center;
    }
    
    .benefit-icon {
      margin-right: 0;
      margin-bottom: 1rem;
    }
  }
  
  @media (max-width: 768px) {
    .about_page {
      padding: 1rem;
    }
    
    .top1-title h1 {
      font-size: 2rem;
    }
    
    .top2-introduction h2 {
      font-size: 1.5rem;
    }
    
    .contact-form {
      padding: 0 1rem;
    }
  }
  </style>