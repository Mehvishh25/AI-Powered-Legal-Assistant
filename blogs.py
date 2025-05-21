import streamlit as st

def run():
    st.markdown("""
        <h1 style='font-size:60px;'>
            <span style='background: linear-gradient(to right, #0B3D2E, #4CAF50); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Explore Legal Knowledge </span>⚖️
        </h1>
    """, unsafe_allow_html=True)

    st.write("""
        Discover insightful legal information, guides, and resources to help you understand your rights and responsibilities. 
        Stay informed and empowered with trustworthy legal education.
    """)

    st.markdown(f"""
        <div style='background:linear-gradient(to right,#defcfc,#e0f5e0);border-radius: 15px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
          <h3 style='font-size: 26px; font-weight: bold; color: #0B3D2E; margin-bottom: 15px;text-align:center'>Legal Blogs 📚</h3>
          <div style='display: flex; flex-wrap: wrap; gap: 15px;'>
            <!-- First Blog -->
            <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
                <a href="https://www.lawfareblog.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #0B3D2E; text-decoration: none; display: block; background: linear-gradient(to right, #f0f9f0, #d9f0d9); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>Lawfare Blog</a>
                <div style='font-size: 14px; color: #555; margin-top: 5px;'>- By Benjamin Wittes</div>
                <div style='font-size: 14px; color: #555;'>Analysis on legal issues in national security, law, and policy.</div>
            </div>   
            <!-- Second Blog -->
            <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
                <a href="https://www.scotusblog.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #0B3D2E; text-decoration: none; display: block; background: linear-gradient(to right, #f0f9f0, #d9f0d9); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>SCOTUSblog</a>
                <div style='font-size: 14px; color: #555; margin-top: 5px;'>- By Amy Howe and staff</div>
                <div style='font-size: 14px; color: #555;'>Comprehensive coverage of the Supreme Court of the United States.</div>
            </div>       
            <!-- Third Blog -->
            <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
                <a href="https://www.legalzoom.com/blog" target="_blank" style='font-size: 18px; font-weight: bold; color: #0B3D2E; text-decoration: none; display: block; background: linear-gradient(to right, #f0f9f0, #d9f0d9); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>LegalZoom Blog</a>
                <div style='font-size: 14px; color: #555; margin-top: 5px;'>- By LegalZoom Team</div>
                <div style='font-size: 14px; color: #555;'>Tips and guides on personal legal issues and small business law.</div>
            </div>
            <!-- Fourth Blog -->
            <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); margin-top: 0;'>
                <a href="https://www.abajournal.com" target="_blank" style='font-size: 18px; font-weight: bold; color: #0B3D2E; text-decoration: none; display: block; background: linear-gradient(to right, #f0f9f0, #d9f0d9); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>ABA Journal</a>
                <div style='font-size: 14px; color: #555; margin-top: 5px;'>- By American Bar Association</div>
                <div style='font-size: 14px; color: #555;'>Latest legal news, analysis, and commentary for lawyers and the public.</div>
            </div>       
            <div style='flex: 1 1 calc(33.33% - 10px); background-color: #ffffff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); margin-top: 0;'>
                <a href="https://www.nolo.com/legal-encyclopedia" target="_blank" style='font-size: 18px; font-weight: bold; color: #0B3D2E; text-decoration: none; display: block; background: linear-gradient(to right, #f0f9f0, #d9f0d9); padding: 15px; border-radius: 10px; transition: all 0.3s ease-in-out; margin-bottom: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);'>Nolo Legal Encyclopedia</a>
                <div style='font-size: 14px; color: #555; margin-top: 5px;'>- By Nolo</div>
                <div style='font-size: 14px; color: #555;'>Comprehensive legal information on a wide range of topics for everyday people.</div>
            </div>
         </div>
         </div>

         <div style='background-color: #ffffff; border-radius: 15px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);'>
             <h3 style='font-size: 26px; font-weight: bold; color: #0B3D2E; margin-bottom: 15px;'>Legal Educational Videos 🎥</h3>
             <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px;'>
                  <!-- First Video -->
                  <div style='background: #f0f9f0; border-radius: 10px; padding: 10px;'>
                       <img src="https://img.youtube.com/vi/r_JI4KbEy1k/hqdefault.jpg" style="width: 100%; border-radius: 10px;" />
                       <a href="https://www.youtube.com/watch?v=r_JI4KbEy1k" target="_blank" style="font-size: 16px; font-weight: bold; color: #0B3D2E; text-decoration: none;">Understanding Contracts Basics</a>
                       <div style="font-size: 14px; color: #555;">1.1M views</div>
                  </div>
                  <!-- Second Video -->
                  <div style='background: #f0f9f0; border-radius: 10px; padding: 10px;'>
                       <img src="https://img.youtube.com/vi/K65DEXrR9As/hqdefault.jpg" style="width: 100%; border-radius: 10px;" />
                       <a href="https://www.youtube.com/watch?v=K65DEXrR9As" target="_blank" style="font-size: 16px; font-weight: bold; color: #0B3D2E; text-decoration: none;">Laws</a>
                       <div style="font-size: 14px; color: #555;">700K views</div>
                  </div>
                  <!-- Third Video -->
                  <div style='background: #f0f9f0; border-radius: 10px; padding: 10px;'>
                       <img src="https://img.youtube.com/vi/dBo9SzzbugA/hqdefault.jpg" style="width: 100%; border-radius: 10px;" />
                       <a href="https://www.youtube.com/watch?v=dBo9SzzbugA" target="_blank" style="font-size: 16px; font-weight: bold; color: #0B3D2E; text-decoration: none;">How Courts Work</a>
                       <div style="font-size: 14px; color: #555;">900K views</div>
                  </div>
             </div>
         </div>
    """, unsafe_allow_html=True)
