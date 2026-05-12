#!/usr/bin/env python3
"""
Inject standardized Related Guides + cross-category light links into all articles.
Run from repo root: python3 scripts/inject-links.py
"""
import re

# --- TEMPLATES ---

DRYER_RELATED = '''
        <section class="section" style="margin-top:32px;">
        <h2>Related Wavytalk Hair Dryer Guides</h2>
        <div class="link-card-grid">
            <a href="wavytalk-ionic-hair-dryer-review" class="link-card">
                <div>
                    <span class="link-card-title">Wavytalk Hair Dryer Review</span>
                    <div class="link-card-meta">4.4&#9733; &middot; 24,197 reviews &middot; $33 &middot; #1 Best Seller</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
            <a href="how-to-use-a-diffuser" class="link-card">
                <div>
                    <span class="link-card-title">How to Use the Diffuser Attachment</span>
                    <div class="link-card-meta">Step-by-step for defined, frizz-free curls</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
            <a href="wavytalk-hair-dryer-for-curly-hair" class="link-card">
                <div>
                    <span class="link-card-title">Wavytalk Hair Dryer for Curly Hair</span>
                    <div class="link-card-meta">Diffuser results and technique for 2A-3C curls</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
            <a href="wavytalk-hair-dryer-attachments" class="link-card">
                <div>
                    <span class="link-card-title">Wavytalk Hair Dryer Attachments Explained</span>
                    <div class="link-card-meta">Comb, diffuser, concentrator: which one fits your hair?</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
        </div>
        <p style="margin-top:16px; font-size:14px; color:#555;">If your hair is already dry and your main issue is frizz or puffiness, see our <a href="wavytalk-pro-steam-straightener-review" style="color:#e8527a; font-weight:600;">Wavytalk Pro Steam Straightener review</a>.</p>
        </section>
'''

STEAM_RELATED = '''
        <section class="section" style="margin-top:32px;">
        <h2>Related Wavytalk Steam Straightener Guides</h2>
        <div class="link-card-grid">
            <a href="wavytalk-pro-steam-straightener-review" class="link-card">
                <div>
                    <span class="link-card-title">Wavytalk Pro Steam Straightener Review</span>
                    <div class="link-card-meta">4.5&#9733; &middot; 4,277 reviews &middot; $67 &middot; Amazon's Choice</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
            <a href="how-to-use-wavytalk-steam-straightener" class="link-card">
                <div>
                    <span class="link-card-title">How to Use Wavytalk Steam Straightener</span>
                    <div class="link-card-meta">From unboxing to salon results in 15 minutes</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
            <a href="steam-straightener-vs-flat-iron" class="link-card">
                <div>
                    <span class="link-card-title">Steam Straightener vs Flat Iron</span>
                    <div class="link-card-meta">Head-to-head: damage, speed, results compared</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
            <a href="wavytalk-steam-straightener-for-thick-hair" class="link-card">
                <div>
                    <span class="link-card-title">Wavytalk Steam Straightener for Thick Hair</span>
                    <div class="link-card-meta">Settings, timing, and real buyer results on dense textures</div>
                </div>
                <span class="link-card-action">Read &rarr;</span>
            </a>
        </div>
        <p style="margin-top:16px; font-size:14px; color:#555;">If your main issue is drying wet hair after washing, see our <a href="wavytalk-ionic-hair-dryer-review" style="color:#e8527a; font-weight:600;">Wavytalk Hair Dryer review</a>.</p>
        </section>
'''

# --- FILES ---

DRYER_FILES = [
    'wavytalk-ionic-hair-dryer-review.html',
    'best-ionic-hair-dryers-2026.html',
    'how-to-use-a-diffuser.html',
    'wavytalk-hair-dryer-for-thick-hair.html',
    'wavytalk-hair-dryer-for-curly-hair.html',
    'wavytalk-hair-dryer-for-4c-hair.html',
    'wavytalk-hair-dryer-attachments.html',
    'ionic-hair-dryer-vs-regular-hair-dryer.html',
    'how-to-reduce-frizz-when-blow-drying.html',
    'wavytalk-hair-dryer-not-for-thin-hair.html',
]

STEAM_FILES = [
    'wavytalk-pro-steam-straightener-review.html',
    'wavytalk-steam-straightener-4c-hair.html',
    'best-steam-straighteners-2026.html',
    'steam-straightener-vs-flat-iron.html',
    'how-to-use-steam-straightener.html',
    'wavytalk-steam-straightener-for-thick-hair.html',
    'wavytalk-steam-straightener-for-fine-hair.html',
    'wavytalk-steam-straightener-for-frizzy-hair.html',
    'how-to-use-wavytalk-steam-straightener.html',
    'can-you-use-wavytalk-steam-straightener-on-wet-hair.html',
    'does-wavytalk-steam-straightener-damage-hair.html',
    'why-does-steam-straightener-pull-hair.html',
]

def remove_existing_related(html):
    """Remove existing Related Reading/Articles/Guides sections (the last H2 with Related + its content up to </section> or </article>)"""
    # Pattern: find last occurrence of <h2>Related ... </h2> followed by content until next </section> or </article>
    # We'll remove everything from that h2 to the closing </section> tag (if within a section) or to </article>
    # Strategy: find all h2 with "Related" in them and remove the containing feature-grid/link-card block
    
    # Remove section blocks that contain "Related" h2s
    pattern = r'\s*<(?:section[^>]*|h2[^>]*)>Related[^<]*</(?:section|h2)>.*?(?=\s*</article>|\s*<section|\s*<div class="disclosure")'
    # Simpler: just remove from "<h2>Related" to the next "</section>" or right before "</article>"
    # Let's be more precise - remove the entire last "Related" block
    
    # Find and remove: <h2>Related...</h2> + <div class="feature-grid">...</div> or <div class="link-card-grid">...</div>
    # Pattern that matches the Related section at the end of articles
    patterns = [
        # Matches: <h2>Related...</h2> ... </div>\n    </section>\n (section wrapper)
        r'\s*<section class="section"[^>]*>\s*<h2>Related[^<]*</h2>.*?</section>',
        # Matches standalone h2 + feature-grid (no section wrapper)
        r'\s*<h2>Related[^<]*</h2>\s*<div class="(?:feature-grid|link-card-grid)"[^>]*>.*?</div>\s*(?:</div>\s*)*',
    ]
    
    for pat in patterns:
        html = re.sub(pat, '', html, flags=re.DOTALL)
    
    return html

def inject_related(html, related_block):
    """Inject the related block right before </article>"""
    # Insert before the last </article> tag
    insertion_point = html.rfind('    </article>')
    if insertion_point == -1:
        insertion_point = html.rfind('</article>')
    
    if insertion_point == -1:
        print("  WARNING: No </article> found!")
        return html
    
    return html[:insertion_point] + related_block + '\n' + html[insertion_point:]

def process_files(files, related_block, category_name):
    for fname in files:
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                html = f.read()
            
            # Remove existing related sections
            cleaned = remove_existing_related(html)
            
            # Inject new standardized block
            result = inject_related(cleaned, related_block)
            
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(result)
            
            print(f"  ✓ {fname}")
        except FileNotFoundError:
            print(f"  ✗ {fname} NOT FOUND")
        except Exception as e:
            print(f"  ✗ {fname}: {e}")

print("=== Injecting Hair Dryer Related Guides ===")
process_files(DRYER_FILES, DRYER_RELATED, "Hair Dryer")

print("\n=== Injecting Steam Straightener Related Guides ===")
process_files(STEAM_FILES, STEAM_RELATED, "Steam Straightener")

print("\nDone!")
